# Bowl Inverter – Automatic Alternating Bowl Flipper

Engineering repository for the automatic bowl inverter developed in the 2026-08-26 design session.

## Goal

All bowls enter upright. Output must alternate:

`UP / DOWN / UP / DOWN / ...`

at **160 bowls/min**.

## Important geometry correction

The product taper direction was corrected on 2026-08-26:

- **Bottom / conveyor-contact diameter: 138 mm**
- **Top diameter: 120 mm**
- Height: **62 mm**
- Mass: **87 g**

This correction invalidates the old V6/V10.10/V11 geometry PASS claims until the guide, screw and roller paths are regenerated.

Read [`docs/GEOMETRY_CORRECTION_2026-08-26.md`](docs/GEOMETRY_CORRECTION_2026-08-26.md) before using historical CAD validation numbers.

## Read these first

1. [`docs/CURRENT_ENGINEERING_BASELINE.md`](docs/CURRENT_ENGINEERING_BASELINE.md) – current source of truth.
2. [`docs/GEOMETRY_CORRECTION_2026-08-26.md`](docs/GEOMETRY_CORRECTION_2026-08-26.md) – corrected Ø138-bottom / Ø120-top geometry and its consequences.
3. [`docs/CONVERSATION_SUMMARY.md`](docs/CONVERSATION_SUMMARY.md) – historical technical recap.
4. [`docs/DECISIONS_AND_FAILURES.md`](docs/DECISIONS_AND_FAILURES.md) – rejected concepts and failure reasons.
5. [`data/current_baseline.json`](data/current_baseline.json) – machine-readable current baseline.
6. [`docs/CODEX_HANDOFF.md`](docs/CODEX_HANDOFF.md) – handoff rules for Codex/another agent.
7. [`docs/UPLOAD_STATUS.md`](docs/UPLOAD_STATUS.md) and [`cad/README.md`](cad/README.md) – artifact status and CAD lineage.

## Timing relations retained

At the 160 bowls/min baseline:

- Bowl interval: **0.375 s**
- Flip event interval: **0.75 s**
- Pitch: **160 mm**
- Axial speed: **426.667 mm/s**
- Single-start timing screw: **160 rpm**
- 3-arm rotor: **26.667 rpm**
- Screw rotation per bowl: **360°**
- Rotor rotation per bowl: **60°**
- Rotor rotation per flip event: **120°**

These timing formulas remain valid after the product geometry correction.

## Mechanism principle retained

1. Timing screw meters every bowl and remains the longitudinal phase master.
2. Lift/return guide raises and tilts the bowl toward a provisional pre-flip angle.
3. Even after the bowl is fully off the conveyor, the timing screw must still provide positive longitudinal drive.
4. Non-selected bowls return toward upright while still screw-driven.
5. Selected bowls are engaged by a correctly phased transfer roller/paddle.
6. Receiving guide positively controls the crossover/inversion; no uncontrolled free flight.
7. Transfer relief opens only after positive takeover.
8. The screw transfer region remains circumferentially asymmetric so return-side drive material survives.

## Current geometry-validation status

**REVALIDATION REQUIRED.**

The previous V11 screw and V10.10 roller-clearance checkpoint were generated with the wrong taper direction.

A diagnostic using the corrected bowl on old trajectories found approximately:

- RETURN old-path minimum bowl-to-shaft clearance: **2.58 mm**
- FLIP old-path minimum bowl-to-shaft clearance: **4.11 mm**

The previous target was >=5 mm, so historical geometry must not be treated as current PASS evidence.

Historical V6/V10.10/V11 artifacts are preserved for engineering history and comparison only.

## Simulation status

- V12 original: had a continuous-spawning bug where bowls disappeared after running briefly.
- V12.1: spawning logic corrected using absolute product index/parity.
- V12.3: viewer uses **Ø138 bottom / Ø120 top**, clearer conveyor surfaces, 16:9 frame and adjustable bowls/min playback timing.

V12.3 is currently an orientation/continuity preview, **not** clearance/contact design evidence until corrected mechanical trajectories are regenerated.

## Sanity check

Run:

```bash
python scripts/validate_baseline.py
```

Expected current result: timing/metadata sanity PASS plus explicit message that **mechanical geometry revalidation is required**.

Binary recovery can be checked with:

```bash
python scripts/verify_binary_hashes.py
```

## Critical rules

- Correct product geometry is Ø138 bottom / Ø120 top.
- Do not rely on conveyor traction after the bowl is lifted off the belt.
- Do not release the timing screw too early.
- Do not open full transfer relief before positive takeover.
- Do not neck down the full screw circumference in the transfer region.
- Do not use uncontrolled free flight.
- Do not let wrong/non-active rollers touch bowls.
- Do not accept rigid-body geometric penetration.
- Do not create fake bowl rotation in the viewer; motion must be trajectory driven.
- Do not treat AI concept renders as engineering geometry.

## Next engineering work

1. regenerate corrected bowl envelope and pose trajectories;
2. regenerate lift/return and receiving guides;
3. regenerate timing screw with positive-drive validation;
4. recompute shaft/transfer clearances;
5. refit the selected roller contact path;
6. rerun multi-bowl collision/phase sweep;
7. create a new corrected-geometry PASS checkpoint.

This repository is an engineering-development checkpoint, not a released manufacturing drawing set.
