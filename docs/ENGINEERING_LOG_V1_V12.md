# Engineering Log V1 → V12

This document preserves the engineering reasoning and decisions from the bowl inverter design session. It is intentionally detailed so that future work does not silently revert to rejected mechanisms.

## 1. Product and production requirement

Product:

- sealed dry pho/noodle bowl
- top/mouth diameter = 138 mm
- bottom diameter = 120 mm
- height = 62 mm
- mass = 87 g
- incoming orientation = upright, bottom on conveyor
- approximate body = truncated cone

Target:

- throughput = 160 bowls/min
- output sequence = upright / inverted / upright / inverted / ...
- bowl period = 60 / 160 = 0.375 s
- only every second bowl flips, therefore flip-event period = 0.75 s

Baseline product geometry:

- top radius = 69 mm
- bottom radius = 60 mm
- taper angle = atan((69-60)/62) ≈ 8.26 deg
- radial profile can be approximated as R(z) = 60 + 9*z/62, z=0..62 mm

CG of the packed product was not measured. Earlier estimates assumed CG height roughly 26–36 mm, giving approximate tipping angles around 59–67 deg. Therefore the ~52 deg pre-tilt used during development is a conservative provisional design value, not a measured final optimum.

## 2. Fundamental mechanism selected

The final concept is NOT based on a bowl freely self-rotating around a screw and is NOT a decorative animation.

The selected mechanical sequence is:

1. bowl enters a timing screw
2. timing screw meters/advances the bowl
3. a lift guide beside the screw raises the bowl and progressively tilts it
4. while lifted completely off the conveyor, the timing screw STILL advances the bowl and holds phase
5. at the pre-flip region, every other bowl is selected by a phased roller/paddle
6. selected bowl is pushed laterally through a transfer opening in the timing screw
7. receiving guide takes control after the tipping transition and completes/controls inversion
8. non-selected bowl remains on the original side and is returned to upright by a return guide
9. output alternates upright/inverted

No uncontrolled free flight is allowed.

## 3. Critical positive-drive requirement

This is the most important mechanical constraint discovered during the session.

When the lift guide has raised the bowl fully away from the conveyor:

- belt normal force is zero
- axial advance force must still come primarily from the timing screw
- lift/return guide supports weight and controls vertical/lateral pose
- guide friction must not be relied upon to synchronize axial motion

Therefore the screw pocket must preserve a directional drive flank on the trailing side of the bowl.

Conceptual force allocation:

- screw → Fx (longitudinal drive and phase)
- guide → Fz (support) plus lateral constraint
- paddle/roller + receiving guide → transfer control after takeover

The screw must NOT open transfer relief too early.

Required sequence:

CAPTURE → METERING → LIFT + POSITIVE DRIVE → PRE-FLIP → PADDLE CONTACT → CONTROL OVERLAP → TRANSFER RELIEF → CROSSOVER → RECEIVING GUIDE → RELEASE.

There must be positive-control overlap before the screw relinquishes control.

## 4. Baseline timing

Baseline pitch selected around the transfer region:

- pitch = 160 mm
- single-start screw = 160 rpm

Axial speed:

V = 160 mm/rev × 160 rev/min / 60 = 426.667 mm/s.

This exactly corresponds to one 160 mm product pitch every 0.375 s.

Rotor baseline:

- 3 arms
- one flip event every 0.75 s
- 120 deg arm spacing
- required average rotor speed = 80 flip events/min / 3 = 26.667 rpm

At this speed:

- rotor rotates 60 deg per bowl interval
- rotor rotates 120 deg per flip-event interval

## 5. V1 – initial screw sections

V1 created section targets around bowl tilt stations 0 / 15 / 30 / 45 / 52 deg.

Initial baseline at that point included:

- pitch 160 mm
- 160 rpm
- early blank OD estimate around 120 mm
- shaft around 25 mm
- drive-side axial clearance target around 1.5 mm
- leading-side clearance around 4 mm

Important result: geometry could be described station-by-station in the rotating screw frame rather than using a simple standard helix.

Key design lesson:

A symmetric “subtract bowl envelope + clearance” groove is not sufficient. The groove needs an asymmetric positive drive flank.

## 6. V2 / V2.1 – flip branch after pre-tilt

The selected-bowl branch was divided into:

- PRE_FLIP around X=640 mm, about 52 deg
- paddle first contact around X=670
- overlap mid around X=705
- overlap end around X=740
- relief opens around X=780
- bowl crosses screw-axis region around X=840
- paddle releases later
- bowl settles toward 180 deg

Representative V2.1 values:

| Station | X mm | Bowl angle | Lateral shift | Screw control |
|---|---:|---:|---:|---|
| PRE_FLIP | 640 | 52 deg | 0 | full drive |
| FIRST_CONTACT | 670 | 52 deg | 0 | full drive |
| OVERLAP_MID | 705 | 58 deg | 15 mm | full drive |
| OVERLAP_END | 740 | 65 deg | 35 mm | full drive last |
| RELIEF_OPEN | 780 | 78 deg | 58 mm | trailing lug only |
| CROSS_AXIS | 840 | 110 deg | 100 mm | screw released |
| PADDLE_RELEASE | ~875 | ~145 deg | ~116 mm | paddle release |
| SETTLED | ~920 | 180 deg | ~120 mm | exit |

The major transfer relief must not open before the paddle and receiving guide have positive control.

## 7. V3 – return branch and dual-path screw

The non-selected bowl also reaches the pre-tilt region but is not pushed laterally.

Return branch baseline:

- X=640: about 52 deg, lift ~47 mm
- X=705: ~48.9 deg
- X=740: ~42.6 deg
- X=780: ~32.0 deg
- X=800: ~26 deg
- X=840: ~14.3 deg
- X=880: ~5.4 deg
- X=920: ~0.8 deg
- X=960: 0 deg, returned to conveyor

This led to the key “dual-path screw” insight:

At the same axial station the screw must simultaneously:

- preserve a return-side drive lug/flank for the non-selected bowl
- open a crossover window in another circumferential sector for the selected bowl

Therefore DO NOT create a full-circumference neck-down or relief.

The transfer section must be asymmetric around the screw circumference.

## 8. V4 – first swept-envelope 3D screw

V4 generated a real swept-envelope screw prototype using both bowl trajectories in the rotating screw frame.

Useful result:

- showed that a crossover window and return-side material could coexist
- section checks around X=740 / 780 / 840 showed material remained on the return side

But V4 was NOT final.

Major correction discovered later:

The Ø120 assumption was too small to keep positive drive through the highly lifted region. The screw could have material in a section without that material being located correctly to drive the bowl.

Therefore “material remains” is not enough; the drive flank must be checked specifically in the longitudinal force direction.

## 9. V5.1 – positive-drive correction

The screw concept was revised with a larger blank and shifted axis.

Development baseline moved toward:

- blank around Ø135 mm
- shaft Ø25 mm
- screw center shifted toward bowl
- later corrected final axis around Y=-21.5 mm, Z=26.5 mm

Another important correction:

Opening the 6 mm transfer relief immediately at the 52 deg branch split cut away useful drive material too early.

Fix:

- retain the full/strong drive flank through the early overlap
- begin major relief later
- preserve a trailing drive lug until takeover is established

V5.1 local contact checks were reported as passing the positive-drive stations used in that iteration.

## 10. V6 – lift/return guide + receiving guide + paddle contact path

V6 generated geometry/paths for:

- lift/return guide
- receiving guide
- desired paddle contact path

The guides were derived from the calculated bowl pose trajectory rather than arbitrary visual curves.

Important observation:

The required paddle contact path is not a perfect fixed-radius circular arc. Therefore a simple fixed rigid three-arm wheel cannot be assumed to follow the desired contact trajectory exactly.

## 11. V7 – first real paddle fitting attempt

A broad/simple paddle concept was fitted against the V6 path.

This iteration showed that broad paddle geometry was not satisfactory because the real contact path is non-circular and the rigid envelope can interfere with product.

Conclusion:

Do not lock a broad rectangular paddle just because it is easy to model.

## 12. V8 – curved 3D paddle study

V8 generated a narrow curved paddle path instead of a broad plate.

Reported screening from that study included:

- selected bowl geometric clearance roughly 0.17–4.66 mm in the kinematic model
- minimum adjacent unflipped bowl clearance roughly 61.6 mm

This was useful for proving that a narrow shaped contact member could avoid the neighboring bowl, but it was not considered a final force-applying mechanism.

## 13. V9 – connected rotor/hanger prototype

V9 connected the curved contact member to a 3-arm rotor through an outboard hanger/link concept.

Reported preliminary clearances:

- selected bowl to lower link ~5.55 mm minimum
- selected bowl to vertical post ~25.6 mm minimum
- unflipped bowls to hanger structure around ~70 mm

Again, this was a kinematic structure concept, not stress-optimized hardware.

## 14. V10 series – multi-bowl dynamic screening

The V10 sequence is important because several FAIL results corrected modeling mistakes and unsafe geometry.

### V10 initial issues

Early multi-bowl checking found failures including:

- wrong screw-axis value being used in one dynamic check
- only bowl #0/arm #0 initially being classified as intended contact, causing false collision classification
- rigid paddle geometry penetrating the selected bowl
- other rotor arms contacting bowls when they were not retracted

These FAIL iterations are deliberately preserved as engineering evidence.

### Rule established by user

Rigid geometry must not be allowed to overlap product.

For the selected bowl, only intentional tangent contact is acceptable. Penetration/interference is not acceptable.

Wrong/non-selected arms must not contact any bowl.

### Selective roller evolution

The actuation concept evolved toward a roller/follower on a cam-controlled arm rather than a large fixed rigid paddle.

One useful intermediate linear-cam study reported:

- roller radius around 8 mm
- main slider travel around 78.6 mm
- small normal correction around 2.34 mm
- tangent contact error approximately within ±0.1 mm in the point-cloud model

But wrong-arm interference still existed unless inactive rollers were physically retracted.

### V10.10 high-retract selective roller

The important final V10 concept:

- only the correctly phased arm descends into the product/flip window
- inactive rollers park above the product envelope at about Z=170 mm
- positive rotor arm arrival order in the model = 0 → 2 → 1
- active contact duration ≈0.225 s
- approach and retract around 0.14 s each in the studied cam law

Reported V10.10 checks:

- unflipped bowl to any roller: ~79.36 mm minimum clearance
- flip bowl to wrong roller: ~95.05 mm minimum clearance
- assigned roller contact approximately -0.09 to +0.07 mm in the discrete point-cloud model; interpreted as tangent zero-gap within discretization tolerance, not allowed design penetration
- neighbor bowl clearance carried forward: ~22 mm
- shaft clearance carried forward: ~5.09 mm

V10.10 was marked preliminary PASS for kinematic/contact-envelope screening.

Important limitation:

This is not yet a contact-force solver. Friction, product deformation, roller force, acceleration, impact load, bearing load, shaft deflection, fatigue and food-machine construction are not finalized.

## 15. V11 – regenerated final-axis timing screw

V11 regenerated the timing screw around the corrected final axis instead of translating the V5.1 solid.

Final baseline reported in the session:

- blank OD = 135 mm
- shaft OD = 25 mm
- screw axis = Y=-21.5 mm, Z=26.5 mm
- pitch = 160 mm
- approximately 92 swept product poses used to generate the geometry

Reported V11 validation:

- positive-drive stations PASS
- shaft margin minimum reported around 12.45 mm in the V11 regenerated-solid validation
- transfer-section material remained present at the checked stations

This V11 regenerated screw is the preferred CAD baseline over V4/V5.1.

## 16. V12 – web playback

V12 generated a browser-based 3D playback using the calculated FLIP/RETURN bowl trajectories and line speeds.

Important status: V12 IS NOT FINISHED.

Known bug reported by user:

> bowls move for a short time and then disappear

Likely class of bug:

- object spawning/recycling/window logic in playback is incomplete
- bowls leave the modeled machine window and are not continuously respawned/recycled correctly

Therefore V12 should not be treated as final simulation evidence until fixed.

The user also rejected generated “nice looking” 3D concept images because they showed the wrong mechanism principle. Those images must be treated only as rejected visual references, never as geometry or proof of operation.

## 17. Current trusted architecture

Use this architecture unless a later validated redesign explicitly replaces it:

- one timing screw as longitudinal phase/master element
- lift/return guide co-designed with screw
- bowl remains positively driven by screw after leaving belt
- pre-tilt around ~52 deg is provisional
- non-selected bowl returns to 0 deg on original side
- selected bowl is transferred laterally through an asymmetric screw window
- receiving guide prevents uncontrolled free flight
- 3-arm rotor at 26.667 rpm is synchronized to 80 flip events/min
- only the correct arm/roller enters the product zone
- inactive rollers retract clear of all bowls
- selected contact is tangent/controlled, not CAD overlap

## 18. Parameters considered locked vs provisional

### Relatively locked for current checkpoint

- bowl top Ø138 mm
- bowl bottom Ø120 mm
- bowl height 62 mm
- bowl mass 87 g
- rate 160 bowls/min
- pitch 160 mm baseline
- line speed 426.667 mm/s
- screw 160 rpm baseline
- flip period 0.75 s
- 3-arm rotor 26.667 rpm baseline
- screw must retain positive longitudinal drive after lift-off
- no uncontrolled free flight
- no wrong-arm contact
- no rigid geometric interference
- final-axis V11 baseline Y=-21.5 mm / Z=26.5 mm
- V11 blank Ø135 / shaft Ø25 baseline

### Still provisional / must be physically validated

- exact CG location of real packaged bowl
- exact optimum pre-tilt angle (52 deg is provisional)
- guide contact bands and wear strips
- surface materials and friction coefficients
- true paddle/roller contact force law
- cam acceleration/jerk and actuator sizing
- structural shaft/rotor/bearing sizing
- food-grade material and washdown details
- final transfer clearances/tolerance stack
- final CNC screw surface and machining relief
- bowl compliance/deformation under contact

## 19. Required physical validation before manufacturing freeze

1. Measure actual CG distribution over real product samples.
2. Measure bowl stiffness and permissible sidewall/rim contact load.
3. Measure static/dynamic friction for proposed guide, screw and bowl surfaces.
4. Run rigid-body + compliant-contact simulation or physical prototype.
5. Verify no lid/rim damage at 160 bowls/min.
6. Validate screw torque and shaft deflection.
7. Validate rotor bearing loads and cam/follower acceleration.
8. Add adjustment range for product dimensional tolerance.
9. Check sanitation, access, guarding, drainage and cleaning.
10. Only then freeze manufacturing drawings.

## 20. Immediate next engineering tasks

1. Fix V12 continuous bowl spawning/recycling so bowls never disappear unexpectedly.
2. Rebuild viewer with the correct mechanism principle, not generated illustrative geometry.
3. Use V11 regenerated screw as the master screw CAD.
4. Build a true tangent-contact roller/cam model with force/acceleration constraints.
5. Add real physical bowl material/CG data.
6. Run multi-cycle collision validation over multiple consecutive bowls.

