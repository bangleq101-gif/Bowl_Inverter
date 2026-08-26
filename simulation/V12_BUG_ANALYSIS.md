# V12 playback bug: bowls disappear after running for a while

## Symptom

The V12 browser playback initially shows bowls moving through the machine, but after enough runtime the bowls leave the visible machine window and no new bowls appear.

This is a **viewer spawning/indexing bug**, not evidence that the mechanical trajectory itself ends.

## Root cause

The V12 frame loop used an ever-increasing reference position:

```js
let xref = 706 + DATA.params.v * t;
for (let i = -12; i <= 3; i++) {
  let x = xref + i * DATA.params.pitch;
  if (x < -180 || x > 1120) continue;
  bowlWire(x, (i % 2) === 0);
}
```

`xref` increases forever because `t` increases forever. The index range is fixed to only `-12..3`. Eventually even `xref - 12*pitch` is larger than the right side of the machine window, so every candidate is rejected and the screen contains no bowls.

At 160 bowls/min:

- product speed = 426.667 mm/s
- pitch = 160 mm

The animation therefore needs an **unbounded bowl sequence or a phase-wrapped spawning scheme**, not a finite set of offsets attached to an ever-growing reference.

## Correct spawning rule

For each frame, compute the bowl indices that intersect the visible machine interval.

Example:

```js
const X_MIN = -180;
const X_MAX = 1120;
const P = DATA.params.pitch;
const V = DATA.params.v;

function drawBowls(t) {
  // Bowl n=0 is defined at x=0 when t=0.
  // Every integer n represents a real continuously arriving bowl.
  const base = V * t;

  const nMin = Math.floor((X_MIN - base) / P) - 1;
  const nMax = Math.ceil((X_MAX - base) / P) + 1;

  for (let n = nMin; n <= nMax; n++) {
    const x = base + n * P;
    if (x < X_MIN || x > X_MAX) continue;

    // Absolute bowl parity must be preserved. Do not use a temporary
    // screen-local index if it changes when the visible window shifts.
    const flip = (n & 1) === 0;
    bowlWire(x, flip);
  }
}
```

An alternative is to phase-wrap the reference position:

```js
const phaseX = ((V * t) % P + P) % P;
```

and generate enough integer pitch offsets to cover the visible range. If that method is used, an independent integer cycle counter must preserve global odd/even bowl parity so the `UP/DOWN` assignment does not swap when the phase wraps.

## Important engineering rule

The fix must only repair **product spawning/playback**. It must not alter the validated bowl pose functions for COMMON / RETURN / FLIP, screw speed, rotor speed, or mechanical phase simply to make the animation look continuous.

## V12.1 acceptance criteria

1. Run at least 60 s with no disappearing product stream.
2. Visible pitch remains 160 mm.
3. New bowls continuously enter from the left as old bowls exit the right.
4. Absolute alternating assignment remains stable: return / flip / return / flip...
5. Screw remains 160 rpm.
6. Rotor remains 26.667 rpm.
7. Rotor arm sequence remains the current modeled order `0 -> 2 -> 1`.
8. Viewer pose for every bowl is still sampled from the validated trajectory data; no decorative self-rotation is introduced.
9. A counter should expose total bowls spawned, current visible bowls, returned bowls and flipped bowls so continuity can be verified numerically.

## Status

This bug was identified after the user observed that bowls run for a short time and then disappear. V12 must not be marked final until this spawning fix has been implemented and soak-tested.
