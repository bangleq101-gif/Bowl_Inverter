# Next Work Plan

## Priority 1 — Fix V12 playback bug

Observed bug: bowls run for a short time and then disappear.

Required fix:

1. Use continuous bowl spawning based on global time and pitch, not a finite static list.
2. Compute each bowl index from `floor((x_ref + vt)/pitch)` over the visible machine window.
3. Keep a rolling population before infeed and after outfeed so the viewer never has an empty interval.
4. Assign flip parity from global bowl index, not from local object lifetime.
5. Map every flip bowl to the correct rotor arm phase.
6. Destroy/recycle only objects outside the useful world window.
7. Add a debug overlay: bowl id, branch, x, theta, assigned arm.
8. Add collision indicators driven by validation data.

Acceptance:

- Run >= 60 s without bowls disappearing.
- Output remains alternating upright/inverted.
- No phase jump when objects are recycled.
- Viewer geometry reflects validated V10.10/V11 principles.

## Priority 2 — Make viewer mechanically faithful

The viewer must show:

- timing screw as the longitudinal master;
- lift/return guide;
- selected vs non-selected branches;
- receiving guide;
- only the active roller descending into the product zone;
- inactive rollers parked high;
- correct arm order 0 -> 2 -> 1;
- transfer relief/crossover concept.

Do not use decorative AI render geometry as the mechanism.

## Priority 3 — True contact/force model

Kinematics currently defines where contact should happen, but not the required force.

Need:

- real product CG distribution;
- bowl stiffness/deformation;
- friction coefficients;
- guide normal forces;
- roller contact force;
- moment required to move CG past tipping point;
- sensitivity to product fill variation.

Output should include force-vs-X/time and required actuator/shaft torque.

## Priority 4 — Structural design

Calculate/check:

- timing screw shaft torsion and bending;
- rotor shaft/bearing loads;
- arm stiffness;
- guide deflection;
- dynamic loads at 160 bowls/min;
- fatigue;
- resonant/vibration risk.

## Priority 5 — Tolerance and adjustability

Introduce manufacturing/assembly variation:

- bowl OD/height variation;
- screw runout;
- guide mounting tolerance;
- shaft/bearing play;
- roller position error;
- conveyor height variation.

Design adjustment mechanisms for:

- screw Y/Z position;
- guide height/lateral offset;
- rotor phase;
- roller depth/contact position;
- receiving guide position.

## Priority 6 — Prototype build gate

Before CNC/final build:

1. Produce updated CAD assembly with real brackets/bearings.
2. Run full collision/tolerance sweep.
3. Build low-speed prototype.
4. Test 40 -> 80 -> 120 -> 160 bowls/min.
5. Record high-speed video and actual failure modes.
6. Update CG/friction/contact assumptions from measurement.
7. Freeze V13/V14 manufacturing geometry only after physical validation.

## Suggested repo milestones

- **V12.1**: playback bug fixed
- **V12.2**: faithful 3D viewer + debug overlays
- **V13**: force/contact model
- **V14**: structural + bearing/shaft design
- **V15**: tolerance/adjustability
- **Prototype A**: low-speed hardware
- **Prototype B**: 160 bowls/min validation
- **Release Candidate**: manufacturing drawings