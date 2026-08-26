# CAD artifact handoff

The engineering session produced multiple STEP/STL checkpoints. The repository currently stores their metadata/checksums but, due to the connector used in the chat session, does not yet contain all binary bytes.

See `docs/BINARY_ARTIFACT_CHECKSUMS.json` for exact size and SHA-256.

## Current preferred CAD checkpoint

### Timing screw V11

Expected filename:

`timing_screw_v11_regenerated.step`

Current baseline:

- blank OD: 135 mm
- shaft OD: 25 mm
- pitch: 160 mm
- corrected axis: Y=-21.5 mm, Z=26.5 mm
- regenerated from bowl swept envelopes in the rotating screw frame
- sampled positive-drive checks: PASS
- sampled shaft checks: PASS

Supporting data:

- `data/v11/timing_screw_v11_report.json`
- `data/v11/timing_screw_v11_validation.csv`
- `data/v11/timing_screw_v11_transfer_sections.csv`

### Current assembly checkpoint

Expected filename:

`bowl_inverter_v11_final_assembly.step`

This assembly should be treated as a development checkpoint rather than a released fabrication model.

## Current transfer actuator checkpoint

Expected files:

- `bowl_inverter_v10_10_high_retract_rotor.step`
- `bowl_inverter_v10_10_assembly.step`

Current concept:

- 3-arm rotor
- 26.667 rpm
- modeled arm order 0 -> 2 -> 1
- only correctly phased arm enters product zone
- inactive rollers retract to about Z=170 mm
- selected roller makes controlled tangent contact
- wrong/non-active rollers must remain clear

## Guide geometry checkpoint

Expected files:

- `bowl_inverter_v6_lift_return_guide.step`
- `bowl_inverter_v6_receiving_guide.step`
- `bowl_inverter_v6_paddle_contact_path.step`
- `bowl_inverter_v6_guides_assembly.step`

The guide geometry was generated from the product trajectory. It is not permission to change the trajectory independently: if the product pose is changed, guide and screw geometry must be revalidated together.

## Historical CAD checkpoints

### V4

- first dual-path swept-envelope screw
- useful for reasoning
- later rejected as final baseline because the OD/axis/contact assumptions were corrected

Expected files:

- `timing_screw_v4_dual_path.step`
- `timing_screw_v4_dual_path.stl`

### V5.1

- improved positive-drive geometry
- replaced V4 as the working screw before final axis correction
- superseded by V11

Expected files:

- `timing_screw_v5_1_positive_drive.step`
- `timing_screw_v5_1_positive_drive.stl`

## Binary verification

After binary files are copied into this repo, run:

```bash
python scripts/verify_binary_hashes.py
```

The script compares local bytes against the exact hashes preserved from the design session.

## Do not infer engineering truth from rendered concept images

AI-generated visualizations are not CAD and some showed the wrong mechanism. Only the validated trajectory/report/CAD lineage above should be used for engineering continuation.
