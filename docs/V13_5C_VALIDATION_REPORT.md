# V13.5c Complete Validation

**Candidate:** `timing_screw_v13_5b_true_envelope_clean.step`

**Overall:** **FAIL — geometry revision required.**

## Gate results

| Gate | Result | Key result |
|---|---|---|
| CAD validity / one solid | PASS | 1 valid solid |
| Screw feed +X / timing | PASS | P=160 mm, 160 rpm -> 426.667 mm/s |
| Actual bowl-to-shaft clearance | PASS | min ~11.025 mm |
| Clearance-envelope to shaft | PASS | min FLIP proxy ~5.894 mm > 5 mm |
| Nominal groove continuity | **FAIL** | hard contact at unsampled stations |
| COMMON/RETURN positive drive | **FAIL as full path** | sampled stations work, scalloped stations do not |
| Selected FLIP positive drive | **FAIL** | trailing lug disappears around X700-X708 |
| Transfer section reserve | WARNING | min fraction 0.1846 at X=780 mm |

## Exact failures

The 12 mm discrete cutters correspond to a screw phase jump of:

`360 * 12 / 160 = 27 deg`

That is too coarse for this changing bowl pose. Exact STEP checks found nominal hard contact (`gap = 0`) at examples such as:

- COMMON X=-120 mm
- COMMON X=40 mm
- RETURN X=800 mm

The selected branch has a second, independent failure. Exact lag tests:

| X | gap at -4 mm lag | gap at -6 mm lag | gap at -8 mm lag |
|---:|---:|---:|---:|
| 688 | 1.794 | 0.000 | 0.000 |
| 700 | 1.979 | 0.183 | 0.000 |
| 708 | 4.465 | 3.231 | 1.622 |

At X708, even an 8 mm lag does not reach the current screw, so the selected-bowl drive flank is no longer a valid positive-drive feature there.

## Root cause

1. Envelope sampling is too sparse.
2. The cavity uses isotropic clearance, which removes too much material from the trailing drive side.
3. The RETURN cavity removes the region needed as the selected FLIP drive lug during the overlap period.

## V13.6 correction direction

The next screw should use:

- dense/adaptive swept-envelope sampling;
- **asymmetric clearance**: small trailing/drive-side clearance and larger leading-side clearance;
- slower RETURN/FLIP divergence while screw positive drive is mandatory;
- deliberate retained trailing lug before relief opening.

A preliminary analytic screen already shows that keeping the selected bowl closer to pre-flip longer and using ~0.5–1.0 mm drive-side clearance can recover a lag-catching flank through the early overlap. That candidate still needs a regenerated STEP and exact validation.
