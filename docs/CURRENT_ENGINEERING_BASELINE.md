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

It must retain a drive flank/lug until roller/paddle and receiving guide have established positive control.

Do not open full relief early.

## Pre-flip branch

Current provisional pre-flip angle remains **~52°** as a starting point, not a frozen value.

With corrected base radius 69 mm, a simple static edge-pivot estimate gives approximate tipping angles:

- CG 26 mm -> **69.35°**
- CG 31 mm -> **65.81°**
- CG 36 mm -> **62.45°**

Thus 52° remains below this simple estimate for the previously assumed CG range. Real packed-product CG must still be measured.

## Selected and return branches

The previously stored X stations and pose trajectories are now **historical references only** until regenerated with the corrected product taper.

The logical control sequence is retained:

1. capture/metering;
2. lift + positive screw drive;
3. pre-flip;
4. selected-bowl transfer contact;
5. positive-control overlap;
6. asymmetric transfer relief;
7. receiving-guide takeover;
8. selected bowl -> inverted output, non-selected bowl -> upright return.

## Rotor/roller – historical V10.10, now stale for corrected product geometry

The concept is retained:

- 3-arm rotor
- baseline timing relation **26.667 rpm at 160 bowls/min**
- only correctly phased roller enters product zone
- inactive rollers retract upward
- intended selected-bowl contact is tangent/controlled contact
- wrong/non-active rollers must not touch any bowl
- rigid geometric penetration is not accepted

However the V10.10 clearance numbers were calculated with the old product surface and must be recomputed after the new bowl trajectory is solved.

## Guide principle retained

1. **Lift/return guide** supports weight and controls pose.
2. **Receiving guide** controls the selected bowl after transfer starts.
3. Guides must not become the primary axial-drive source while the bowl is off the belt.
4. No uncontrolled free flight.

The V6 guide curves themselves are stale and must be regenerated.

## Simulation status

### V12.1

Continuous spawning bug was corrected conceptually by using absolute bowl indexes derived from the visible X window rather than a fixed local index range.

### V12.3

Viewer geometry is corrected to **Ø138 bottom / Ø120 top**, with a clearer conveyor surface and adjustable bowls/min playback timing.

Important: V12.3 is a **geometry-orientation / continuity preview**, not design evidence for guide/screw/roller clearance because the engineering trajectories are still awaiting regeneration.

## Not frozen yet

- real CG and product variation
- regenerated pre-flip/return/flip trajectories
- timing-screw final OD/axis/groove for corrected taper
- exact guide cross-sections
- contact force profile
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

1. corrected product geometry is propagated through all trajectories/CAD;
2. real-product CG and variation are measured;
3. force/contact model is validated;
4. screw/guide/roller collision sweep passes with tolerances;
5. structural loads and deflection pass;
6. physical prototype confirms transfer at target speed;
7. sanitation/material requirements are incorporated.
