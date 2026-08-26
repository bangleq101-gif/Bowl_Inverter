# Known Issues and Rejected Concepts

## Known issue – V12 playback

The current V12 browser playback has a confirmed user-visible bug: bowls move for a short time and then disappear. The likely cause is incomplete spawn/recycle/window logic. Until this is fixed, V12 is only a playback prototype and must not be used as engineering proof.

Required fix:

- continuously spawn/recycle bowls at 0.375 s intervals
- preserve alternating FLIP/RETURN assignment
- keep a stable population across the full modeled machine window
- recycle objects after leaving the outfeed region instead of allowing the scene to become empty
- keep phase locked to screw 160 rpm and rotor 26.667 rpm

## Rejected concept – fake/self-rotation animation

Rejected because it did not represent the real mechanics. A bowl must not rotate simply because the visualization assigns an angle. Bowl pose must come from the designed screw/guide/transfer kinematics.

## Rejected concept – screw releases bowl immediately after lift

Rejected. Once the bowl leaves the belt, the timing screw must still provide longitudinal positive drive and maintain phase. The guide must not become the axial-drive mechanism through friction.

## Rejected concept – transfer relief opened too early

Rejected because opening relief before paddle/receiving-guide takeover destroys positive drive. Preserve a drive flank/lug through the control-overlap region.

## Rejected concept – full-circumference transfer neck-down

Rejected because the non-selected bowl still needs a return-side drive path at the same axial stations where the selected bowl crosses the screw. Transfer geometry must be circumferentially asymmetric.

## Rejected concept – uncontrolled free flight

Rejected. After the selected bowl crosses the tipping transition, receiving guide geometry must maintain control and guide it toward inverted orientation.

## Rejected concept – broad rigid paddle

Early V7/V10 studies showed that a broad/simple paddle could interfere with product and did not naturally match the non-circular desired contact trajectory.

## Rejected concept – allowing rigid paddle penetration because a pad is soft

User explicitly rejected this. CAD solids must not be allowed to overlap product. Intended selected-bowl contact should be tangent/controlled. Wrong arms must remain clear.

## Rejected concept – non-retracted inactive rollers

Multi-bowl checking showed that other arms can collide with other bowls if all rollers remain in the product plane. Current concept retracts inactive rollers high above the product envelope, around Z=170 mm in V10.10.

## Rejected visual references

Some generated attractive 3D concept images showed the wrong mechanism principle. They may be retained only as rejected visual history and must not be used as design geometry, manufacturing reference, or simulation validation.

## Modeling limitations still present

Current PASS statements are kinematic/contact-envelope screening only. The following remain unsolved or unverified:

- real packaged-bowl CG distribution
- product wall/lid deformation
- coefficient of friction
- roller contact force and impact
- cam jerk and follower dynamics
- screw torque and shaft deflection
- rotor/bearing load
- guide wear and thermal effects
- manufacturing tolerance stack
- sanitation/food-machine construction

