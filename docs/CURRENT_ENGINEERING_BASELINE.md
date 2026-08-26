# Current Engineering Baseline

Tài liệu này là baseline hiện tại của dự án. Nếu có mâu thuẫn giữa các file cũ và tài liệu này, ưu tiên tài liệu này cho tới khi có checkpoint mới hơn.

## Product – corrected 2026-08-26

- **Bottom / conveyor-contact diameter: 138 mm**
- **Top diameter: 120 mm**
- Height: **62 mm**
- Mass: **87 g**
- Incoming orientation: upright, Ø138 base on conveyor
- Approximation: truncated cone
- Corrected radius profile, with `z` measured upward from the bottom plane:

`r(z) = 69 - 9*z/62` mm, `0 <= z <= 62`

Taper half-angle magnitude remains **8.259°**, but the taper direction is reversed relative to the older model.

See `docs/GEOMETRY_CORRECTION_2026-08-26.md`.

## Throughput and timing – still valid

- Throughput: **160 bowls/min**
- Bowl interval: **0.375 s**
- Flip event interval: **0.75 s**
- Product pitch: **160 mm**
- Axial line speed: **426.667 mm/s**
- Timing screw speed relation at baseline: **160 rpm**, single-start
- Rotor speed relation at baseline: **26.667 rpm**
- Rotor arms: **3**
- Rotor rotation per bowl: **60°**
- Rotor rotation per flip event: **120°**

These are timing/phase relationships only. They do not preserve the previous CAD/contact validation after the bowl geometry correction.

## Coordinate convention

- X: along production flow
- Y: lateral across timing screw/conveyor
- Z: vertical

Previously used timing-screw axis:

- Y = **-21.5 mm**
- Z = **26.5 mm**

This axis remains a design starting point, not a newly validated final axis for the corrected bowl.

## Geometry-validation status

**CURRENT STATUS: REVALIDATION REQUIRED.**

The old V6/V10.10/V11 geometry was generated using the reversed product taper (Ø120 bottom / Ø138 top). After correcting the product to Ø138 bottom / Ø120 top, those geometry PASS claims are stale.

A diagnostic placement of the corrected bowl on the old trajectories produced approximately:

- RETURN minimum bowl-to-shaft clearance: **2.58 mm**
- FLIP minimum bowl-to-shaft clearance: **4.11 mm**

Both are below the previous >=5 mm target at some sampled positions, therefore the old screw/trajectory set cannot remain the current geometry baseline.

## Timing screw – historical V11, now stale for corrected product geometry

Historical V11 values:

- Blank OD: **135 mm**
- Shaft OD: **25 mm**
- Pitch: **160 mm**
- Corrected-axis checkpoint used Y=-21.5 mm, Z=26.5 mm
- Asymmetric transfer concept retained return-side drive material while selected-bowl relief opened

The **principle remains mandatory**, but the V11 solid must be regenerated from the corrected bowl envelope before a new geometry PASS can be claimed.

### Mandatory screw behavior retained

The screw remains the longitudinal phase master after the bowl leaves the conveyor.

It must retain a drive flank/lug until trigger roller and receiving guide have established positive control.

Do not open full relief early.

## Pre-flip branch

Current provisional pre-flip angle magnitude remains **~52°** as a starting point, not a frozen value.

With corrected base radius 69 mm, a simple static edge-pivot estimate gives approximate tipping angles:

- CG 26 mm -> **69.35°**
- CG 31 mm -> **65.81°**
- CG 36 mm -> **62.45°**

Thus 52° remains below this simple estimate for the previously assumed CG range. Real packed-product CG must still be measured.

The **sign/direction** of the pre-flip angle must be re-solved so it is continuous with the physical selected-bowl CCW inversion branch.

## Selected-bowl rotation direction – corrected 2026-08-26

The selected bowl should visibly invert **counter-clockwise (CCW)** in the current viewer convention. The previous playback showed the selected bowl rotating clockwise and that angular branch is now stale.

For the intended transfer, the trigger gives a small lateral push across the screw rather than forcing the bowl through most of the inversion. With the current engineering axes, if the bowl crosses toward `+Y` and the trigger acts above the center of mass with an approximately lateral force `F_y > 0`, then:

`M_x = r_y F_z - r_z F_y ≈ -r_z F_y < 0`

Therefore the old increasing positive-angle `~+52° -> +180°` selected-bowl branch does not match the intended trigger moment sign. The exact numeric sign depends on coordinate/view convention; the physical requirement is that the V13 angular motion be consistent with the actual force moment and appear CCW in the current viewer.

See `docs/ROTATION_DIRECTION_CORRECTION_2026-08-26.md`.

## Transfer actuator – revised role

The selected-bowl roller/paddle is now treated as a **brief tangent trigger**, not a continuous flipping paddle.

Required control sequence:

1. screw + lift guide retain positive control to pre-flip;
2. trigger roller gives only enough lateral impulse/displacement to initiate crossover/tipping;
3. receiving guide captures the bowl early;
4. receiving-guide geometry + gravity/contact reaction control most of the CCW inversion;
5. trigger retracts early;
6. no free flight and no rigid penetration.

The old V10.10 contact window of ~0.225 s is **not** a requirement anymore. V13 must minimize and re-solve the contact interval from actual geometry/force needs.

## Selected and return branches

The previously stored X stations and pose trajectories are now **historical references only** until regenerated with the corrected product taper and CCW selected-bowl branch.

The logical control sequence is retained:

1. capture/metering;
2. lift + positive screw drive;
3. pre-flip;
4. brief selected-bowl trigger contact;
5. positive-control overlap;
6. asymmetric transfer relief;
7. early receiving-guide takeover;
8. selected bowl -> CCW inverted output, non-selected bowl -> upright return.

## Rotor/roller – historical V10.10, now stale for corrected product geometry

The concept is retained:

- 3-arm rotor
- baseline timing relation **26.667 rpm at 160 bowls/min**
- only correctly phased roller enters product zone
- inactive rollers retract upward
- intended selected-bowl contact is brief tangent/controlled trigger contact
- wrong/non-active rollers must not touch any bowl
- rigid geometric penetration is not accepted

However the V10.10 clearance numbers and long contact path were calculated with the old product surface/direction and must be recomputed after the new bowl trajectory is solved.

## Guide principle retained

1. **Lift/return guide** supports weight and controls pose.
2. **Receiving guide** must take over the selected bowl early and control most of the inversion after the trigger.
3. Guides must not become the primary axial-drive source while the bowl is off the belt.
4. No uncontrolled free flight.

The V6 guide curves themselves are stale and must be regenerated.

## Simulation status

### V12.1

Continuous spawning bug was corrected conceptually by using absolute bowl indexes derived from the visible X window rather than a fixed local index range.

### V12.3

Viewer geometry was corrected to **Ø138 bottom / Ø120 top**, with a clearer conveyor surface and adjustable bowls/min playback timing.

### V12.4 direction preview

Viewer selected-bowl angular display is changed to **CCW** to preview the corrected physical direction. This remains a direction/concept preview only: center paths, guides, screw and roller geometry are still historical until V13 regeneration.

## Not frozen yet

- real CG and product variation
- exact pre-flip sign/magnitude
- regenerated CCW return/flip trajectories
- timing-screw final OD/axis/groove for corrected taper
- exact guide cross-sections
- trigger contact point/force/duration
- roller geometry/material
- rotor bearing arrangement
- shaft sizing
- stiffness/fatigue
- sanitation design
- tolerance stack
- adjustment mechanisms
- final CNC-ready screw surface

## Manufacturing gate

Do not release for fabrication until at least:

1. corrected product geometry and CCW rotation direction are propagated through all trajectories/CAD;
2. real-product CG and variation are measured;
3. force/contact model is validated;
4. screw/guide/roller collision sweep passes with tolerances;
5. structural loads and deflection pass;
6. physical prototype confirms transfer at target speed;
7. sanitation/material requirements are incorporated.
