# Current Engineering Baseline

Tài liệu này là baseline hiện tại của dự án. Nếu có mâu thuẫn giữa các file cũ và tài liệu này, ưu tiên tài liệu này cho tới khi có checkpoint mới hơn.

## Product

- Top diameter: **138 mm**
- Bottom diameter: **120 mm**
- Height: **62 mm**
- Mass: **87 g**
- Incoming orientation: upright
- Approximation: truncated cone

## Throughput and timing

- Throughput: **160 bowls/min**
- Bowl interval: **0.375 s**
- Flip event interval: **0.75 s**
- Product pitch: **160 mm**
- Axial line speed: **426.667 mm/s**
- Timing screw speed: **160 rpm**
- Timing screw: single-start baseline
- Rotor speed: **26.667 rpm**
- Rotor arms: **3**
- Rotor rotation per bowl: **60°**
- Rotor rotation per flip event: **120°**

## Coordinate convention

- X: along production flow
- Y: lateral across timing screw/conveyor
- Z: vertical

Current corrected timing-screw axis:

- Y = **-21.5 mm**
- Z = **26.5 mm**

## Timing screw baseline – V11

- Blank OD: **135 mm**
- Shaft OD: **25 mm**
- Pitch: **160 mm**
- Screw surface generated from bowl swept-envelope around the corrected axis
- Transfer region is circumferentially asymmetric
- Return-side drive material must remain while selected-bowl crossover relief opens

### Mandatory screw behavior

The screw remains the longitudinal phase master after the bowl leaves the conveyor.

It must retain a drive flank/lug until paddle/roller and receiving guide have established positive control.

Do not open full relief early.

## Pre-flip branch

Current pre-flip angle baseline: **~52°**.

This is still provisional because the true packed-product CG has not been measured.

## Selected bowl branch – conceptual station sequence

Approximate station logic used during development:

| X (mm) | Bowl state | Control state |
|---:|---|---|
| ~640 | ~52° | screw full drive + lift guide |
| ~670 | first transfer contact | screw still full drive |
| ~705 | ~58° | receiving guide begins takeover |
| ~740 | ~65° | last full-drive region |
| ~780 | ~78° | trailing drive lug + transfer relief |
| ~840 | ~110° | bowl crosses screw-axis region |
| ~875 | ~145° | transfer actuator releases |
| ~920 | ~180° | inverted/output branch |

These X values are development stations, not frozen manufacturing dimensions.

## Non-selected return branch

The non-selected bowl remains on the original side of the screw and returns from pre-flip toward upright.

The timing screw continues positive longitudinal drive while the return guide controls angle/height.

The transfer relief must not remove this return-side drive path.

## Rotor/roller baseline – V10.10

Current actuation concept:

- 3-arm rotor
- Average speed: **26.667 rpm**
- Arm event interval: **0.75 s**
- Active transfer-contact interval: about **0.225 s**
- Modeled arm arrival order for the chosen rotation: **0 -> 2 -> 1**
- Only the correctly phased roller enters the product zone
- Inactive rollers retract upward to approximately **Z=170 mm**
- Intended contact is tangent/controlled contact
- Geometric penetration is not accepted

### V10.10 screening values

- Unflipped bowl to any roller minimum clearance: ~**79.36 mm**
- Flip bowl to wrong roller minimum clearance: ~**95.05 mm**
- Neighbor bowl minimum clearance: ~**22 mm**
- Bowl to screw shaft clearance carried forward: ~**5.09 mm**
- Assigned roller active contact: near zero gap within point-cloud tolerance

## Contact definitions

### Unselected bowl / wrong roller

Must remain separated. No touch allowed.

### Selected bowl / assigned roller

Contact is intentional because force is required to transfer/flip the bowl. The requirement is **tangent controlled contact without solid penetration**.

## Guide baseline

Two logical guide functions are retained:

1. **Lift/return guide** – raises/tilts all bowls toward pre-flip; non-selected bowls then return to upright.
2. **Receiving guide** – receives the selected bowl after transfer begins and prevents uncontrolled free flight.

Guides control support/pose. They must not become the primary axial-drive mechanism while the bowl is off the belt.

## Simulation status

### Engineering CAD/trajectory

- V10.10: preliminary kinematic/contact-envelope PASS
- V11 screw: regenerated final-axis baseline

### V12 web playback

**Known FAIL / incomplete**:

- bowl spawning/window loop is incomplete;
- bowls can disappear after the playback runs for a short time;
- viewer is not approved as design evidence yet.

## Not frozen yet

The following are NOT manufacturing-frozen:

- true CG and product variation
- final pre-flip angle
- exact guide cross-sections
- contact force profile
- roller material and diameter
- rotor bearing arrangement
- shaft sizing for final torque/deflection
- stiffness/fatigue
- sanitation design
- tolerance stack
- adjustment mechanisms
- final CNC-ready screw surface after physical prototype validation

## Manufacturing gate

Do not release for fabrication until at least:

1. real-product CG and variation are measured;
2. force/contact model is validated;
3. screw/guide/paddle collision sweep passes with tolerances;
4. structural loads and deflection pass;
5. physical prototype confirms transfer at target speed;
6. sanitation/material requirements are incorporated.