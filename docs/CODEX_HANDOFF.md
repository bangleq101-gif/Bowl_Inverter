# Codex / agent handoff

Use this file when assigning the Bowl Inverter repository to another coding or engineering agent.

## Mandatory read order

Before modifying anything, read:

1. `README.md`
2. `docs/CONVERSATION_SUMMARY.md`
3. `docs/CURRENT_ENGINEERING_BASELINE.md`
4. `docs/DECISIONS_AND_FAILURES.md`
5. `docs/KNOWN_ISSUES_AND_REJECTED_CONCEPTS.md`
6. `docs/NEXT_WORK_PLAN.md`
7. `simulation/V12_BUG_ANALYSIS.md`
8. `data/current_baseline.json`
9. V11 and V10.10 reports/data referenced by the baseline

Then run:

```bash
python scripts/validate_baseline.py
```

Do not implement a new mechanism before understanding why prior versions failed.

## Mechanical source-of-truth rules

The following constraints are deliberate and must not be silently relaxed:

- All input bowls are upright.
- Required output is alternating upright/inverted.
- 160 bowls/min.
- 160 mm pitch.
- Bowl interval 0.375 s.
- Flip event interval 0.75 s.
- Timing screw 160 rpm baseline.
- 3-arm transfer rotor 26.667 rpm baseline.
- When a bowl is lifted completely off the conveyor, the timing screw must still provide positive longitudinal drive and phase control.
- Do not substitute lift-guide friction for timing-screw axial drive.
- The screw must not release the bowl before transfer takeover.
- The transfer region must preserve return-side drive material while opening selected-bowl crossover clearance.
- No uncontrolled free flight.
- Non-selected/wrong rollers do not touch bowls.
- Intended transfer contact is controlled tangent contact, not CAD penetration.
- Viewer motion must be generated from the validated product pose data; do not fake rotation for visual effect.

## Current accepted checkpoints

### V11 timing screw

- blank OD 135 mm
- shaft OD 25 mm
- pitch 160 mm
- corrected axis Y=-21.5 mm, Z=26.5 mm
- generated from swept product envelopes in the rotating screw frame
- positive-drive sampled validation PASS
- sampled shaft validation PASS

### V10.10 transfer actuator

- selective high-retract roller concept
- 3 arms
- 26.667 rpm
- modeled arm order 0 -> 2 -> 1
- active contact window about 0.225 s
- inactive rollers retract to roughly Z=170 mm
- current checkpoint is kinematic/contact-envelope PASS, not final production validation

## Current next software task: V12.1

The old V12 browser playback contains a known spawning bug: after enough time all bowls leave the visible window and no new products are generated.

Do not redesign the mechanism to fix this.

Use:

- `simulation/V12_BUG_ANALYSIS.md`
- `simulation/v12_spawn_fix.js`

V12.1 must preserve absolute bowl parity so the alternating assignment never swaps when animation phase wraps.

Minimum acceptance:

- 60 s continuous run with product always present in the machine window;
- pitch remains 160 mm;
- continuous infeed/outfeed;
- stable return/flip alternation;
- screw remains 160 rpm;
- rotor remains 26.667 rpm;
- product pose remains trajectory-driven;
- no decorative self-rotation.

## Engineering maturity

Do not call the project fabrication-ready yet.

Still required:

- packed product center-of-gravity measurement and distribution;
- friction tests;
- bowl stiffness/deformation measurements;
- transfer contact force/torque calculation or measurement;
- shaft, bearing, rotor and guide structural checks;
- tolerance stack and adjustment strategy;
- hygiene/material/fabrication detailing;
- physical prototype validation up to 160 bowls/min.

## Versioning discipline

For every new version:

1. State the problem being addressed.
2. State assumptions.
3. State what changed from previous version.
4. Define quantitative acceptance criteria before claiming PASS.
5. Record FAIL results instead of deleting them.
6. Add machine-readable validation data when possible.
7. Update `CURRENT_ENGINEERING_BASELINE.md` and `current_baseline.json` only if the new version is accepted as the new source of truth.
8. Add SHA-256 to the binary manifest for new STEP/STL/archive artifacts.

## Worktree / branch safety

Use a dedicated branch/worktree for each substantial feature or mechanical version. Before modifying files, verify the current repository, branch and worktree. Do not use destructive cleanup/reset operations that could remove another active worktree.

## Suggested first command sequence

```bash
git status
git branch --show-current
git worktree list
python scripts/validate_baseline.py
```

Then inspect V12 spawning logic. The first useful deliverable should be V12.1 continuity, not a new cosmetic render.
