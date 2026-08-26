# Geometry correction – 2026-08-26

## Correct product orientation

The previously stored product taper direction was wrong.

Correct incoming bowl geometry is now:

- **Bottom / conveyor-contact diameter: 138 mm**
- **Top diameter: 120 mm**
- Height: **62 mm**
- Mass: **87 g**
- Incoming orientation: upright, Ø138 base on the conveyor

With `z` measured upward from the bottom plane (`0 <= z <= 62 mm`), the corrected radius profile is:

`r(z) = 69 - 9*z/62` mm

The taper half-angle magnitude remains:

`atan(9/62) = 8.259°`

but its direction is reversed relative to the old model.

## Timing formulas that remain valid

The geometry correction does **not** change the line timing relationships by itself.

At 160 bowls/min and 160 mm pitch:

- bowl interval = `60/160 = 0.375 s`
- line speed = `160 / 0.375 = 426.667 mm/s`
- single-start screw baseline = **160 rpm** -> 360° per bowl
- one flip every two bowls -> flip event interval = **0.75 s**
- 3-arm rotor baseline = `80/3 = 26.667 rpm`
- rotor rotation per bowl = **60°**
- rotor rotation per flip event = **120°**

Those are timing/phase relations, not proof that the previous CAD still clears the corrected bowl.

## Static tipping estimate

Using the simple edge-pivot estimate `theta_tip = atan(Rbase / hCG)` with corrected base radius `Rbase=69 mm`:

| assumed CG height | tipping estimate |
|---:|---:|
| 26 mm | 69.35° |
| 31 mm | 65.81° |
| 36 mm | 62.45° |

The provisional 52° pre-flip angle therefore remains below this simple static tipping estimate for the previously assumed CG range. This does **not** freeze 52°; real packed-product CG still needs measurement.

## Diagnostic re-check of old trajectories

The corrected bowl surface was placed on the old COMMON/RETURN/FLIP pose trajectories only as a diagnostic.

Approximate results:

- neighbor-bowl minimum clearance remains about **22 mm** in the sampled old trajectory set;
- minimum bowl-to-shaft clearance on the old RETURN trajectory drops to about **2.58 mm**;
- minimum bowl-to-shaft clearance on the old FLIP trajectory drops to about **4.11 mm**.

The shaft criterion used previously was >=5 mm, so the old geometry is no longer acceptable.

## Consequence

The following must be treated as **stale / pending revalidation** for the corrected bowl geometry:

- V6 lift/return guide path;
- V6 receiving-guide/contact path;
- V10.10 roller/contact clearance results;
- V11 timing-screw swept envelope and its geometry PASS claim;
- V12 playback geometry based on those old paths.

Do not delete those versions: they remain useful engineering history. But do not cite their clearance/contact PASS results as current after this correction.

## Current next step

1. Regenerate bowl envelope using Ø138 bottom / Ø120 top.
2. Re-solve lift/pre-flip/return trajectories.
3. Regenerate timing screw around the corrected trajectory while preserving positive axial drive.
4. Recompute transfer relief, shaft clearance and return-side drive lug.
5. Re-fit selected roller/receiving guide and re-run multi-bowl collision sweep.
6. Only then create a new geometry PASS checkpoint.
