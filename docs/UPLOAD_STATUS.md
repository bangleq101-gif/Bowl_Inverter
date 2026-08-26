# Upload status – engineering checkpoint 2026-08-26

This file distinguishes what is **actually stored in GitHub** from what is only tracked by metadata/checksum.

## 1. Already stored in GitHub and authoritative for the current checkpoint

### Core documentation

- `README.md`
- `docs/CONVERSATION_SUMMARY.md`
- `docs/CURRENT_ENGINEERING_BASELINE.md`
- `docs/DECISIONS_AND_FAILURES.md`
- `docs/ENGINEERING_LOG_V1_V12.md`
- `docs/KNOWN_ISSUES_AND_REJECTED_CONCEPTS.md`
- `docs/NEXT_WORK_PLAN.md`
- `docs/ARTIFACT_MANIFEST.md`
- `docs/BINARY_ARTIFACT_CHECKSUMS.json`

### Machine-readable baseline / reports

- `data/current_baseline.json`
- `data/analysis_snapshot.json`
- `data/v10/v10_10_report.json`
- `data/v11/timing_screw_v11_report.json`
- `data/v11/timing_screw_v11_validation.csv`
- `data/v11/timing_screw_v11_transfer_sections.csv`
- trajectory data under `data/trajectories/`
- historical JSON checkpoints under `data/history/`
- archived small station/contact tables in `data/archive/historical_small_artifacts.json`

### Simulation/debug source

- `simulation/v12_report.json`
- `simulation/V12_BUG_ANALYSIS.md`
- `simulation/v12_spawn_fix.js`

### Regression checks

- `scripts/validate_baseline.py`
- `scripts/README.md`

## 2. Binary CAD / mesh artifacts – NOT yet stored as repository bytes

The current GitHub connector available in this chat exposes UTF-8/string based file writes but does not expose a direct local-binary upload action. Therefore the following files are **not to be claimed as uploaded binaries** merely because their hashes are in the repository.

Their exact byte counts and SHA-256 values are recorded in `docs/BINARY_ARTIFACT_CHECKSUMS.json`.

Important current files include:

- `timing_screw_v11_regenerated.step`
- `timing_screw_v11_regenerated.stl`
- `bowl_inverter_v11_final_assembly.step`
- `bowl_inverter_v10_10_high_retract_rotor.step`
- `bowl_inverter_v10_10_assembly.step`
- `bowl_inverter_v6_lift_return_guide.step`
- `bowl_inverter_v6_receiving_guide.step`
- `bowl_inverter_v6_paddle_contact_path.step`
- `bowl_inverter_v6_guides_assembly.step`
- historical V4 / V5.1 screw STEP/STL files

Until those bytes are pushed through a binary-capable Git workflow, the checksums are the traceability reference.

## 3. V12 HTML

The generated V12 HTML is a historical prototype and currently contains the documented product-spawning bug. The root cause and patch are preserved in the repository.

Do **not** promote the old V12 viewer as final evidence. The next viewer should be V12.1 or later and must pass the continuous-spawn soak test.

## 4. AI-generated images

Several concept/illustration images were generated during the discussion. Some were explicitly judged by the user to show the wrong mechanical principle.

They are therefore **not engineering source geometry** and should never be used to infer dimensions, clearances, trajectories, or fabrication details.

If archived later, place them under a clearly named path such as:

`images/concept_only/`

with a disclaimer in that directory.

## 5. What counts as the current source of truth

When documents disagree, use this priority:

1. `docs/CURRENT_ENGINEERING_BASELINE.md`
2. `data/current_baseline.json`
3. V11 validation/report files for timing screw geometry
4. V10.10 report for current transfer actuator checkpoint
5. `docs/DECISIONS_AND_FAILURES.md`
6. historical files only for reasoning/history

## 6. Rule for future uploads

Every new CAD or simulation checkpoint should include:

- version number;
- purpose;
- assumptions;
- acceptance criteria;
- validation result;
- failure reason if rejected;
- exact SHA-256 for binary artifacts;
- an update to the current baseline only after the new version is actually accepted.

Never overwrite the reason a previous version failed.
