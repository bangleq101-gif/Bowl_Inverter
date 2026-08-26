# V13 corrected-bowl / CCW trigger-flip trajectory report

**Status:** kinematic trajectory screen PASS; CAD screw/guide solid, rotor-cam fit, forces and physical prototype are still pending.

## Locked inputs
- Bowl: Ø138 bottom / Ø120 top / H62 / 87 g.
- Pitch: 160 mm; 160 bowls/min; axial speed 426.667 mm/s.
- Single-start screw timing: 160 rpm. 3-arm trigger rotor timing relation: 26.667 rpm.
- Theta sign: negative = CCW in the current viewer/mechanical convention.

## Pose laws
`S5(s)=10s^3-15s^4+6s^5`.

- COMMON 0→640 mm: `theta=-52*S5`, `cy=-115+39*S5-7*sin²(pi*s)`, `cz=31+65*S5`.
- RETURN 640→960 mm: `theta=-52*(1-S5)`, `cy=-76-39*S5-7*sin²(pi*s)`, `cz=96-65*S5`.
- FLIP 640→940 mm: `theta=-52-128*S5`, `cy=-76+201*S5`, `cz=96-65*S5+45*sin²(pi*s)`.
- At x≥940 selected bowl is settled at `theta=-180°, cy=125, cz=31`.

## Dense cross-section checks
- COMMON min shaft clearance: **11.025 mm** at X=415 mm.
- RETURN min shaft clearance: **11.025 mm** at X=752 mm.
- FLIP min shaft clearance: **11.096 mm** at X=640 mm.
- Design screening target: **≥10.0 mm nominal**.
- Longitudinal bowl-to-bowl geometric clearance: `160 - 2*69 = **22 mm**`.
- Bowl never goes below conveyor plane in the ideal trajectory.

## Why a light trigger is mechanically consistent
At 52° the bowl is still statically stable. Using a bottom-rim pivot and CG height h, the neutral angle is `atan(69/h)`:
- h=26 mm → 69.35° (trajectory reaches it near X=723 mm).
- h=31 mm → 65.81° (near X=716 mm).
- h=36 mm → 62.45° (near X=708 mm).

Therefore the trigger does **not** need to force the whole 52→180° inversion. It only starts the CCW motion. Receiving guide starts at X=675 mm, overlaps trigger for **35.2 ms**, trigger releases at X=690 mm, and the receiving guide then carries the bowl through the neutral/tipping region (~X 709–724 mm). Gravity assists after that.

## Trigger contact
- Active X: 660→690 mm = **70.3 ms** at 160 bowls/min.
- Desired contact: upper outer rim `C=(-60,+31)` in bowl local coordinates.
- Force direction: approximately +Y.
- `Mx/Fy=-r_z`, so the generated moment is negative / CCW.
- Uniform-solid-frustum inertia screen: `Ix≈0.000118944 kg·m²`.
- Ideal inertial force component: ~**0.045 N**; nominal gravity-resistance equivalent near trigger start: ~**0.226 N**. These are only lower-bound physics checks; friction, bowl flex, package CG and guide losses require real testing.

## Control overlap
1. X640–660: selected pre-trigger; lift support + screw full drive.
2. X660–675: light trigger starts; screw still full drive.
3. X675–690: trigger + receiving guide overlap + screw full drive.
4. X690–710: trigger off; receiving guide established; screw still full drive.
5. X710–760: asymmetric selected-side relief opens while receiving guide controls; return-side drive lug must remain.
6. X760–940: receiving guide completes CCW inversion; selected screw sector is released.
7. X940+: inverted bowl settled on output belt.

## Dynamic screen at 160 bowls/min
- COMMON duration 1.500 s; max angular speed 65.0 deg/s.
- RETURN duration 0.750 s; max angular speed 130.0 deg/s.
- FLIP duration 0.703 s; max angular speed 341.3 deg/s.
- Geometry is X-based. If rate changes, velocities scale ∝ rate and accelerations ∝ rate².

## Still mandatory before manufacturing
- Regenerate timing-screw swept-envelope/CAD from these corrected trajectories.
- Build receiving/lift/return guide solids with real thickness and tolerance.
- Fit the 3-arm cam/roller mechanism to the new short trigger path and re-run wrong-arm clearance.
- Measure actual packed-bowl CG and friction.
- Multibody/contact or physical prototype test; then shaft/bearing/guide stress and sanitation review.
