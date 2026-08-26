# Artifact Manifest – 2026-08-26 checkpoint

This manifest records the artifacts generated during the engineering session. The engineering meaning of these files is documented in `ENGINEERING_LOG_V1_V12.md`.

## V1–V5 timing-screw development

- `timing_screw_v1_sections.json`
- `timing_screw_transfer_v2_1.json`
- `timing_screw_transfer_v2_1_stations.csv`
- `timing_screw_transfer_v2_stations.csv`
- `timing_screw_v3_return_branch.json`
- `timing_screw_v3_return_stations.csv`
- `timing_screw_v4_dual_path.step`
- `timing_screw_v4_dual_path.stl`
- `timing_screw_v4_pose_samples.csv`
- `timing_screw_v4_preview.svg`
- `timing_screw_v4_report.json`
- `timing_screw_v4_section_x740.step`
- `timing_screw_v4_section_x780.step`
- `timing_screw_v4_section_x840.step`
- `timing_screw_v4_slab_check.json`
- `timing_screw_v5_1_contact_local.csv`
- `timing_screw_v5_1_contact_local_report.json`
- `timing_screw_v5_1_positive_drive.step`
- `timing_screw_v5_1_positive_drive.stl`

## V6 guide development

- `bowl_inverter_v6_guide_paths.csv`
- `bowl_inverter_v6_guides_assembly.step`
- `bowl_inverter_v6_lift_return_guide.step`
- `bowl_inverter_v6_paddle_contact_path.step`
- `bowl_inverter_v6_receiving_guide.step`
- `bowl_inverter_v6_report.json`

## V7 paddle fitting

- `bowl_inverter_v7_cam_profile.csv`
- `bowl_inverter_v7_contact_table.csv`

## V8 curved paddle study

- `bowl_inverter_v8_assembly.step`
- `bowl_inverter_v8_clearance.csv`
- `bowl_inverter_v8_curved_paddle_shoe.step`
- `bowl_inverter_v8_paddle_profile.csv`
- `bowl_inverter_v8_report.json`
- `bowl_inverter_v8_three_arm_rotor_reference.step`

## V9 connected rotor/hanger study

- `bowl_inverter_v9_assembly.step`
- `bowl_inverter_v9_attachment_clearance.csv`
- `bowl_inverter_v9_connected_paddle_unit.step`
- `bowl_inverter_v9_connected_three_arm_rotor.step`
- `bowl_inverter_v9_report.json`

## V10 dynamic / collision studies

The V10 series intentionally includes failed intermediate studies because they explain why later geometry changed.

- `bowl_inverter_v10_dynamic_clearance.csv`
- `bowl_inverter_v10_selected_contact.csv`
- `bowl_inverter_v10_1_dynamic_clearance.csv`
- `bowl_inverter_v10_2_dynamic_clearance.csv`
- `bowl_inverter_v10_2_paddle_profile.csv`
- `bowl_inverter_v10_3_dynamic_clearance.csv`
- `bowl_inverter_v10_3_paddle_profile.csv`
- `bowl_inverter_v10_4_dynamic_clearance.csv`
- `bowl_inverter_v10_4_paddle_profile.csv`
- `bowl_inverter_v10_6_cam_path.csv`
- `bowl_inverter_v10_6_clearance.csv`
- `bowl_inverter_v10_6_no_penetration_clearance.csv`
- `bowl_inverter_v10_6_no_penetration_profile.csv`
- `bowl_inverter_v10_7_dynamic_clearance.csv`
- `bowl_inverter_v10_7_slider_cam.csv`
- `bowl_inverter_v10_8_cam_cycle.csv`
- `bowl_inverter_v10_8_dynamic_clearance.csv`
- `bowl_inverter_v10_9_cam_cycle.csv`
- `bowl_inverter_v10_9_dynamic_clearance.csv`
- `bowl_inverter_v10_10_assembly.step`
- `bowl_inverter_v10_10_cam_cycle.csv`
- `bowl_inverter_v10_10_dynamic_clearance.csv`
- `bowl_inverter_v10_10_high_retract_rotor.step`
- `bowl_inverter_v10_10_report.json`

### V10.10 current preferred rotor checkpoint

V10.10 is the current preferred kinematic rotor/roller checkpoint because inactive rollers retract above the bowl envelope and the correct arm is selectively engaged.

## V11 regenerated timing screw

- `timing_screw_v11_regenerated.step`
- `timing_screw_v11_regenerated.stl`
- `timing_screw_v11_report.json`
- `timing_screw_v11_transfer_sections.csv`
- `timing_screw_v11_validation.csv`
- `bowl_inverter_v11_final_assembly.step`

### V11 current preferred screw checkpoint

Use V11 as the preferred screw geometry baseline. V4 and V5.1 are preserved as development history and should not silently replace V11.

## V12 browser playback

- `bowl_inverter_v12_playback.html`
- `bowl_inverter_v12_report.json`

Known issue: V12 bowls can disappear after a short run because continuous spawn/recycle logic is incomplete.

## Generated concept images

- `bảng_mô_phỏng_máy_đảo_tô_công_nghiệp.png`
- `máy_lật_tô_phở_tự_động_qua_vít_tải.png`

These images are **not engineering-valid geometry**. The user explicitly rejected the visual principle shown in generated 3D imagery. Preserve them only as history of rejected visualization attempts.

## Preferred files for continuation

For the next engineering session, start from:

1. `docs/ENGINEERING_LOG_V1_V12.md`
2. `data/analysis_snapshot.json`
3. V11 regenerated timing-screw geometry/data
4. V10.10 selective high-retract rotor concept/data
5. V6 lift/return + receiving guide trajectories
6. V12 playback only as a viewer prototype that requires bug fixing

