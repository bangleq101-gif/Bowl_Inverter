# Bowl Inverter – Automatic Alternating Bowl Flipper

Engineering repository for the automatic bowl inverter developed in the 2026-08-26 design session.

## Goal

All bowls enter upright. Output must alternate:

`UP / DOWN / UP / DOWN / ...`

at **160 bowls/min**.

## Read these first

1. [`docs/CONVERSATION_SUMMARY.md`](docs/CONVERSATION_SUMMARY.md) – complete technical recap of the conversation, from the initial ideas through V12.
2. [`docs/CURRENT_ENGINEERING_BASELINE.md`](docs/CURRENT_ENGINEERING_BASELINE.md) – current source of truth for dimensions, speeds, mechanism and validation status.
3. [`docs/DECISIONS_AND_FAILURES.md`](docs/DECISIONS_AND_FAILURES.md) – rejected concepts and why each failed. Do not silently reintroduce them.
4. [`docs/NEXT_WORK_PLAN.md`](docs/NEXT_WORK_PLAN.md) – next engineering tasks and acceptance criteria.
5. [`data/current_baseline.json`](data/current_baseline.json) – machine-readable baseline for agents/scripts.
6. [`simulation/V12_BUG_ANALYSIS.md`](simulation/V12_BUG_ANALYSIS.md) – exact root cause of the disappearing-bowl viewer bug and V12.1 acceptance criteria.

## Product

- Top diameter: **138 mm**
- Bottom diameter: **120 mm**
- Height: **62 mm**
- Mass: **87 g**
- Incoming orientation: upright

## Locked line baseline

- Throughput: **160 bowls/min**
- Bowl interval: **0.375 s**
- Flip event interval: **0.75 s**
- Pitch: **160 mm**
- Axial speed: **426.667 mm/s**
- Timing screw: **160 rpm**
- 3-arm rotor: **26.667 rpm**

## Current mechanism principle

1. Timing screw meters every bowl and remains the longitudinal phase master.
2. Lift/return guide raises and tilts the bowl toward a provisional pre-flip angle around 52°.
3. Even after the bowl is fully off the conveyor, the timing screw must still provide positive longitudinal drive.
4. A non-selected bowl follows the return guide back toward upright while the screw continues driving it.
5. A selected bowl is engaged by the correctly phased transfer roller/paddle.
6. Receiving guide positively controls the bowl through the crossover/inversion region; no uncontrolled free flight.
7. Transfer relief opens only after takeover is established.
8. The screw transfer region is asymmetric so return-side drive material remains available while the selected bowl crosses.

## Current timing screw – V11

- Blank OD: **135 mm**
- Shaft OD: **25 mm**
- Corrected axis: **Y=-21.5 mm, Z=26.5 mm**
- Pitch: **160 mm**
- Generated from swept bowl envelopes in the rotating screw frame
- Positive-drive and shaft checks: current V11 report = **PASS**

Key files:

- [`data/v11/timing_screw_v11_report.json`](data/v11/timing_screw_v11_report.json)
- [`data/v11/timing_screw_v11_validation.csv`](data/v11/timing_screw_v11_validation.csv)
- [`data/v11/timing_screw_v11_transfer_sections.csv`](data/v11/timing_screw_v11_transfer_sections.csv)

## Current transfer actuator – V10.10

The broad rigid-paddle approach was rejected. Current concept is a **selective high-retract roller**:

- 3 arms
- 26.667 rpm
- arm order for modeled rotation: **0 -> 2 -> 1**
- active transfer window ≈ **0.225 s**
- inactive rollers retract to about **Z=170 mm** above the product envelope
- assigned roller contact is tangent/controlled contact
- wrong/non-active rollers must not touch any bowl
- rigid geometric penetration is not accepted

Current screening report:

- [`data/v10/v10_10_report.json`](data/v10/v10_10_report.json)

## Simulation status – V12

V12 web playback is **not approved yet**.

Known issue reported during the session:

> bowls run for a short time and then disappear.

Root cause: the old frame loop used an ever-increasing `xref` together with a fixed local index range (`-12..3`). Eventually all candidate bowls moved beyond the visible X window, so no new products were spawned.

The fix is recorded separately so it cannot be confused with a mechanical redesign:

- [`simulation/V12_BUG_ANALYSIS.md`](simulation/V12_BUG_ANALYSIS.md)
- [`simulation/v12_spawn_fix.js`](simulation/v12_spawn_fix.js)
- [`simulation/v12_report.json`](simulation/v12_report.json)

The spawning fix must preserve the absolute bowl index/parity and must not change the validated COMMON / RETURN / FLIP pose data just to make the animation look continuous.

## Regression / sanity check

Run after cloning:

```bash
python scripts/validate_baseline.py
```

The script checks the line timing/phase relationship and the currently stored V11 validation invariants. See [`scripts/README.md`](scripts/README.md).

## Historical development data

Preserved so future work does not lose the reasoning path:

- [`data/history/timing_screw_v1_sections.json`](data/history/timing_screw_v1_sections.json)
- [`data/history/timing_screw_v2_1_transfer.json`](data/history/timing_screw_v2_1_transfer.json)
- [`data/history/timing_screw_v3_return_branch.json`](data/history/timing_screw_v3_return_branch.json)
- [`data/archive/historical_small_artifacts.json`](data/archive/historical_small_artifacts.json) – station/contact tables from multiple intermediate versions.

## CAD / binary artifact traceability

Large CAD/mesh/archive files generated during the session are tracked by exact filename, byte count and SHA-256 in:

- [`docs/BINARY_ARTIFACT_CHECKSUMS.json`](docs/BINARY_ARTIFACT_CHECKSUMS.json)
- [`docs/ARTIFACT_MANIFEST.md`](docs/ARTIFACT_MANIFEST.md)

This prevents later files from being mistaken for the approved checkpoint even when binary transfer/storage is handled separately.

## Critical rules that must not be broken silently

- Do not rely on conveyor traction after the bowl is lifted off the belt.
- Do not release the timing screw too early.
- Do not open full transfer relief before positive takeover.
- Do not neck down the full screw circumference in the transfer region.
- Do not use uncontrolled free flight.
- Do not let wrong/non-active rollers touch bowls.
- Do not accept rigid-body geometric penetration.
- Do not create fake bowl rotation in the viewer; motion must be trajectory driven.
- Do not treat AI concept renders as engineering geometry.

## Current engineering maturity

This is a **kinematic/CAD development checkpoint**, not a released manufacturing drawing set.

Still required before fabrication freeze:

- real packed-product CG/variation
- friction data
- bowl stiffness/deformation
- transfer contact force/torque
- shaft/bearing/arm structural checks
- tolerance stack and adjustability
- sanitation/material detailing
- physical prototype validation up to 160 bowls/min

## Repository note

The repository is intended to be the persistent engineering source of truth. Any new design version should update the baseline, preserve the previous failure reason, and add validation data rather than overwriting the reasoning history.
