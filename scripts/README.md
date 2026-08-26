# Engineering scripts

This directory contains small, auditable helpers for maintaining the Bowl Inverter engineering checkpoint.

## `validate_baseline.py`

Run after cloning:

```bash
python scripts/validate_baseline.py
```

It verifies the repository-level invariants currently considered source-of-truth:

- 160 bowls/min
- 0.375 s per bowl
- 160 mm pitch
- 426.667 mm/s product speed
- 160 rpm timing screw -> 360° per bowl
- 26.667 rpm 3-arm rotor -> 60° per bowl / 120° per flip event
- all sampled V11 positive-drive checks remain PASS
- sampled V11 shaft margin remains at least 10 mm
- transfer sections keep at least 30% of the full annulus material in the sampled sections
- the V10.10 report remains the current preliminary transfer-actuator PASS checkpoint

The script is a regression/sanity check only. It does not replace the original CAD Boolean, swept-envelope, collision or contact calculations.

## Simulation fix

See:

- `simulation/V12_BUG_ANALYSIS.md`
- `simulation/v12_spawn_fix.js`

These preserve the exact root cause and the intended V12.1 spawning correction. The mechanical trajectory data must not be changed merely to make the viewer look continuous.
