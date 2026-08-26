# Flip Rotation Direction Correction – 2026-08-26

## User-observed correction

The selected bowl should not be driven through most of the 52° -> 180° inversion by a broad paddle/roller. The transfer actuator should only give a small lateral trigger/push, after which the receiving guide and gravity/geometry control the inversion.

In the current viewer convention, the physically expected selected-bowl inversion is **counter-clockwise (CCW)**. The previous playback showed the selected bowl rotating clockwise and is therefore not the correct sign convention for the new V13 solve.

## Engineering moment-sign check

Coordinate convention:

- X = production direction / bowl flip axis
- Y = lateral transfer direction across the screw
- Z = vertical

For the selected bowl crossing toward +Y, assume the trigger applies an approximately lateral force `F_y > 0` at a contact point above the bowl center of mass (`r_z > 0`). With negligible vertical trigger force, the moment about X is approximately:

`M_x = r_y F_z - r_z F_y ≈ -r_z F_y`

Therefore `M_x < 0` in the engineering right-hand coordinate system.

The old selected-bowl pose table used an increasing positive angle from about `+52°` to `+180°`. That sign does not match the above trigger moment for the intended contact placement. The V13 trajectory solve must use the opposite rotation sign / geometry branch, while the viewer should present the visible inversion as **CCW**.

Important: the exact numeric angle sign depends on camera/display convention. The physical rule is not the word “negative”; it is that the solved angular motion must be consistent with the actual trigger force moment and the chosen coordinate frame.

## Mechanism change

Treat the selected-bowl actuator as a **trigger roller**, not a continuous flipping paddle.

Desired sequence:

1. Timing screw + lift guide bring the bowl to the pre-flip pose while retaining positive X drive.
2. Trigger roller makes brief tangent contact and supplies only enough lateral impulse/displacement to move the bowl across the stability boundary / into the receiving-guide capture region.
3. Receiving guide establishes positive control before the screw transfer relief fully opens.
4. Bowl continues the CCW inversion under receiving-guide geometry plus gravity/contact reaction.
5. Trigger roller retracts early; it must not remain the primary element forcing the bowl through 110–145°.
6. No free flight and no hard geometric penetration.

## What becomes stale

The following old assumptions must not be carried forward without regeneration:

- the sign of the V2/V6/V10 selected-bowl rotation trajectory;
- the long V10.10 active-contact window as a design requirement;
- the old roller/paddle path that follows the bowl deep into the inversion;
- old receiving-guide contact geometry derived from the clockwise branch.

## V13 requirements

- Solve pre-flip direction and selected-bowl rotation consistently from the corrected Ø138-bottom bowl geometry.
- Define the physical trigger force direction and contact height explicitly.
- Verify `sign(M_x)` from the actual contact point and force vector.
- Minimize trigger contact duration; do not choose a duration merely to match old V10.10.
- Ensure receiving-guide takeover occurs before trigger release / transfer relief causes loss of control.
- Recompute shaft, screw, guide and wrong-roller clearances for the CCW branch.
- Re-run multi-bowl phase/collision checks.
- Only then publish a new geometry/contact PASS checkpoint.

## Viewer status

V12.4 may mirror the displayed bowl angular sign to preview the corrected CCW direction, but it remains a **concept-direction preview** until V13 trajectories are regenerated. Center paths and old guide curves are historical and must not be treated as validated contact geometry.