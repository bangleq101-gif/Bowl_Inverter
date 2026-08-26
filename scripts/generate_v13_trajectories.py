#!/usr/bin/env python3
"""Regenerate V13 corrected-bowl CCW pose/guide tables.

This is a kinematic generator only. It does not generate the final timing-screw
solid or replace multibody/contact/structural validation.
"""
import csv, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data'/'v13'; OUT.mkdir(parents=True,exist_ok=True)
RB,RT,H=69.0,60.0,62.0
PITCH,RATE=160.0,160.0
V=PITCH*RATE/60.0
SY,SZ,SHAFT_R=-21.5,26.5,12.5
A=(-69.0,-31.0); B=(69.0,-31.0); D=(60.0,31.0); C=(-60.0,31.0)

def s5(s):
    s=max(0.0,min(1.0,s)); return 10*s**3-15*s**4+6*s**5

def rot(p,th):
    a=math.radians(th); c=math.cos(a); s=math.sin(a); y,z=p
    return y*c-z*s,y*s+z*c

def world(p,cy,cz,th):
    y,z=rot(p,th); return cy+y,cz+z

def poly(cy,cz,th): return [world(A,cy,cz,th),world(B,cy,cz,th),world(D,cy,cz,th),world(C,cy,cz,th)]

def segdist(p,a,b):
    dx=b[0]-a[0]; dz=b[1]-a[1]; den=dx*dx+dz*dz
    if den<=1e-12:return math.hypot(p[0]-a[0],p[1]-a[1])
    t=((p[0]-a[0])*dx+(p[1]-a[1])*dz)/den; t=max(0,min(1,t))
    return math.hypot(p[0]-(a[0]+t*dx),p[1]-(a[1]+t*dz))

def inside(p,q):
    signs=[]
    for i,a in enumerate(q):
        b=q[(i+1)%len(q)]; cr=(b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
        if abs(cr)>1e-9: signs.append(1 if cr>0 else -1)
    return not signs or all(v==signs[0] for v in signs)

def shaft_gap(cy,cz,th):
    q=poly(cy,cz,th); d=min(segdist((SY,SZ),q[i],q[(i+1)%4]) for i in range(4))
    return (-d if inside((SY,SZ),q) else d)-SHAFT_R

def ext(cy,cz,th):
    q=poly(cy,cz,th); ys=[p[0] for p in q]; zs=[p[1] for p in q]
    return min(ys),max(ys),min(zs),max(zs)

def common(x):
    if x<=0:return 0.0,-115.0,31.0
    s=x/640; q=s5(s)
    return -52*q,-115+39*q-7*math.sin(math.pi*s)**2,31+65*q

def ret(x):
    if x>=960:return 0.0,-115.0,31.0
    s=(x-640)/320; q=s5(s)
    return -52*(1-q),-76-39*q-7*math.sin(math.pi*s)**2,96-65*q

def flip(x):
    if x>=940:return -180.0,125.0,31.0
    s=(x-640)/300; q=s5(s)
    return -52-128*q,-76+201*q,96-65*q+45*math.sin(math.pi*s)**2

def receive(cy,cz,th):
    u=max(0,min(1,(abs(th)-70)/80)); lam=s5(u)
    p=(B[0]+lam*(D[0]-B[0]),B[1]+lam*(D[1]-B[1]))
    y,z=world(p,cy,cz,th); return y,z,lam

def trigger(cy,cz,th):
    y,z=world(C,cy,cz,th)
    return y,z,y-8,z,-(z-cz) # contact, R8 roller center, Mx/Fy arm

def phase(x): return ((x-640)/PITCH*360)%360

def state(br,x):
    if br=='COMMON':return common(x)
    if br=='RETURN':return ret(x)
    return flip(x)

def control(br,x):
    if br=='COMMON':return 'BELT_METERING' if x<0 else 'LIFT_GUIDE+SCREW_FULL_DRIVE'
    if br=='RETURN':
        if x<710:return 'RETURN_GUIDE+SCREW_FULL_DRIVE'
        if x<840:return 'RETURN_GUIDE+RETURN_SIDE_DRIVE_LUG'
        return 'RETURN_GUIDE+METERING_FLANK_REENGAGE'
    if x<660:return 'PRETRIGGER+LIFT+SCREW_FULL_DRIVE'
    if x<675:return 'TRIGGER+LIFT+SCREW_FULL_DRIVE'
    if x<690:return 'TRIGGER+RECEIVING_OVERLAP+SCREW_FULL_DRIVE'
    if x<710:return 'RECEIVING+SCREW_FULL_DRIVE'
    if x<760:return 'RECEIVING+ASYMMETRIC_RELIEF_OPENING'
    if x<940:return 'RECEIVING+SELECTED_SCREW_RELEASED'
    return 'OUTPUT_BELT_INVERTED'

rows=[]
for br,xa,xb in [('COMMON',-160,640),('RETURN',640,1040),('FLIP',640,1040)]:
    for x in range(xa,xb+1,4):
        th,cy,cz=state(br,x); ymin,ymax,zmin,zmax=ext(cy,cz,th)
        rows.append(dict(branch=br,x_mm=x,theta_deg=th,center_y_mm=cy,center_z_mm=cz,
            shaft_clearance_mm=shaft_gap(cy,cz,th),min_bowl_z_mm=zmin,max_bowl_z_mm=zmax,
            min_bowl_y_mm=ymin,max_bowl_y_mm=ymax,screw_phase_deg=phase(x),control_state=control(br,x)))
with (OUT/'v13_trajectories.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)

paths=[]
for x in range(0,641,4):
    th,cy,cz=common(x); y,z=world(A,cy,cz,th); paths.append(dict(path='LIFT_COMMON_A',x_mm=x,y_mm=y,z_mm=z,theta_deg=th,lambda_side='',moment_arm_mm=''))
for x in range(640,961,4):
    th,cy,cz=ret(x); y,z=world(A,cy,cz,th); paths.append(dict(path='RETURN_GUIDE_A',x_mm=x,y_mm=y,z_mm=z,theta_deg=th,lambda_side='',moment_arm_mm=''))
for x in range(640,691,2):
    th,cy,cz=flip(x); y,z=world(A,cy,cz,th); paths.append(dict(path='SELECTED_LIFT_OVERLAP_A',x_mm=x,y_mm=y,z_mm=z,theta_deg=th,lambda_side='',moment_arm_mm=''))
for x in range(675,941,2):
    th,cy,cz=flip(x); y,z,lam=receive(cy,cz,th); paths.append(dict(path='RECEIVING_GUIDE_B_TO_D',x_mm=x,y_mm=y,z_mm=z,theta_deg=th,lambda_side=lam,moment_arm_mm=''))
for x in range(660,691,2):
    th,cy,cz=flip(x); y,z,ry,rz,m=trigger(cy,cz,th)
    paths.append(dict(path='TRIGGER_CONTACT_TOP_RIM_C',x_mm=x,y_mm=y,z_mm=z,theta_deg=th,lambda_side='',moment_arm_mm=m))
    paths.append(dict(path='TRIGGER_ROLLER_CENTER_R8',x_mm=x,y_mm=ry,z_mm=rz,theta_deg=th,lambda_side='',moment_arm_mm=m))
with (OUT/'v13_guide_trigger_paths.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=paths[0].keys());w.writeheader();w.writerows(paths)

# Hard sanity screen at 1-mm X increments.
for br,xa,xb,fn in [('COMMON',-160,640,common),('RETURN',640,960,ret),('FLIP',640,940,flip)]:
    vals=[]
    for x in range(xa,xb+1):
        th,cy,cz=fn(x); vals.append((shaft_gap(cy,cz,th),ext(cy,cz,th)[2],x))
    g=min(vals,key=lambda v:v[0]); z=min(vals,key=lambda v:v[1])
    assert g[0]>=10.0,(br,'shaft gap',g)
    assert z[1]>=-1e-6,(br,'floor',z)
    print(br,'min shaft gap',g[0],'at X',g[2])
assert PITCH-2*RB>=22-1e-9
print('PASS: V13 kinematic cross-section sanity screen')
