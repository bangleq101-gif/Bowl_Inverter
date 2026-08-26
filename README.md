# Bowl Inverter – Automatic Alternating Bowl Flipper

Engineering checkpoint for the automatic bowl inverter developed in ChatGPT on 2026-08-26.

## Goal

Input bowls are all upright. Output must alternate:

`UP / DOWN / UP / DOWN / ...`

at **160 bowls/min**.

## Product data

- Sealed dry-pho/noodle bowl
- Top diameter: **138 mm**
- Bottom diameter: **120 mm**
- Height: **62 mm**
- Mass: **87 g**
- Approximate body: truncated cone
- Incoming state: upright, bottom on conveyor

## Locked line data

- Throughput: **160 bowls/min**
- Bowl interval: **0.375 s**
- Pitch: **160 mm**
- Axial product speed: **426.667 mm/s**
- Timing screw: **160 rpm**, single-start baseline
- Flip event interval: **0.75 s**
- 3-arm rotor: **26.667 rpm**

## Current mechanism principle

1. Every bowl enters the timing screw upright.
2. Timing screw meters and continues to provide **positive longitudinal drive**.
3. A lift/return guide raises and tilts the bowl toward a pre-flip angle (baseline about 52 deg).
4. Even after the bowl is fully off the conveyor, the timing screw must still hold phase and push the bowl forward. The guide must not be relied upon for axial drive by friction.
5. For the bowl that is NOT selected to flip, the return guide brings it from the pre-flip angle back to 0 deg while the timing screw continues to drive it.
6. For the selected bowl, a correctly phased roller/paddle engages only that bowl, moves it laterally through a transfer window in the screw, and the receiving guide controls the remainder of the inversion.
7. There must be no uncontrolled free flight.
8. Wrong/non-active rollers must not touch any bowl.
9. Final output alternates upright/inverted.

## Critical design rule

The timing screw and lift guide are co-designed. The screw must **not release the bowl early**. In the lift/pre-flip region there is a positive-control overlap:

- lift guide: supports weight and controls height/tilt
- timing screw drive flank: continues to generate axial force and maintain phase
- roller/paddle + receiving guide: take over before transfer relief fully opens

Only after the selected bowl is positively controlled by the transfer mechanism may the screw relief open enough for lateral crossover.

## Timing screw status

The final regenerated V11 baseline uses:

- blank OD: **135 mm**
- shaft OD: **25 mm**
- corrected screw axis: **Y = -21.5 mm, Z = 26.5 mm**
- pitch: **160 mm**
- asymmetric transfer section: preserve return-side drive material while opening the selected-bowl crossover sector

V11 was regenerated from the bowl swept envelope around the corrected axis rather than translating the old screw solid.

## Rotor / roller status

The later V10 studies showed that a simple rigid broad paddle was not acceptable. The mechanism evolved toward a selective cam/roller concept.

Current dynamic checkpoint V10.10:

- 3 arms
- rotor speed: **26.667 rpm**
- arm event interval: **0.75 s**
- active roller contact window: about **0.225 s**
- inactive rollers retract to approximately **Z = 170 mm** above the product envelope
- arm order for the modeled positive rotation: **0 -> 2 -> 1**
- intended roller contact is tangent contact; geometric penetration is not accepted

Reported V10.10 screening:

- unflipped bowl to any roller clearance: ~79.36 mm
- selected/other wrong roller clearance: ~95.05 mm
- neighbor bowl clearance carried forward: ~22 mm
- bowl-to-shaft clearance carried forward: ~5.09 mm

These are kinematic/contact-envelope results, not final force, deformation, fatigue, bearing, shaft-stress, sanitation or manufacturing validation.

## Version history / important decisions

- **V1**: initial timing-screw cross-sections and positive-drive concept.
- **V2 / V2.1**: selected-bowl transfer branch from ~52 deg toward 180 deg; overlap -> relief -> crossover.
- **V3**: non-selected return branch ~52 deg -> 0 deg and dual-path/asymmetric screw principle.
- **V4**: first swept-envelope dual-path 3D screw. Useful geometry prototype, but OD/axis/contact assumptions were later corrected.
- **V5.1**: positive-drive screw geometry improved; V4 Ø120 assumption was rejected as too small in lifted region.
- **V6**: lift/return guide, receiving guide and paddle-contact path generated from product trajectory.
- **V7**: first real paddle fitting attempt; broad/simple geometry was not adequate.
- **V8**: curved paddle path study; adjacent unflipped clearance improved, but this was not the final actuation solution.
- **V9**: connected rotor/hanger kinematic prototype.
- **V10 series**: multi-bowl phase/collision studies. Several FAIL iterations are deliberately preserved because they document why broad rigid paddles, wrong phase mapping or non-retracted rollers are unsafe.
- **V10.10**: selective high-retract roller concept reached the current preliminary PASS screening.
- **V11**: timing screw regenerated about corrected final axis; positive drive/shaft/transfer sections rechecked.
- **V12**: web playback prototype. **Known issue:** bowls can disappear after running for a short time because the playback spawning/window logic is incomplete. The current V12 viewer is NOT a final simulation and must be fixed before it is used as design evidence.

## Rejected concepts / do not silently reintroduce

- Do not return to a fake animation where bowls rotate simply because the viewer tells them to rotate.
- Do not rely on belt traction after a bowl is lifted off the conveyor.
- Do not open full transfer relief before paddle/receiving-guide takeover.
- Do not machine a full-circumference neck-down in the transfer region; the non-selected return branch still needs positive drive material.
- Do not use uncontrolled free flight to finish the flip.
- Do not treat rendered concept images as engineering geometry. Some generated illustrations in the discussion were explicitly judged to show the wrong principle.

## Repository layout

- `docs/` – engineering notes and design history
- `data/` – CSV/JSON calculation and validation results
- `cad/` – STEP/STL prototypes and checkpoints
- `simulation/` – HTML playback and simulation data
- `images/` – visual references/concept images, clearly distinguished from engineering CAD
- `archive/` – preserved intermediate artifacts when appropriate

## Next work

1. Fix V12 playback so bowls continuously spawn/loop and never disappear from the useful machine window.
2. Make the 3D viewer use the validated mechanism and correct transfer principle, not decorative generated imagery.
3. Validate true tangent contact/contact force, coefficient of friction, bowl stiffness/deformation and CG distribution.
4. Stress/check shaft, bearings, rotor, guide mounts and screw material.
5. Add adjustability/tolerance stack and food-machine fabrication details.
6. Only after those checks freeze CNC/manufacturing geometry.

This repository is an engineering development checkpoint, not a released manufacturing drawing set.
