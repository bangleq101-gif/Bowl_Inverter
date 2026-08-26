// V12.1 continuous bowl spawning patch
// Purpose: fix disappearing bowls without changing mechanical trajectory data.

export function visibleBowlStates(t, params, xMin = -180, xMax = 1120) {
  const P = params.pitch;
  const V = params.v;
  const base = V * t;

  const nMin = Math.floor((xMin - base) / P) - 1;
  const nMax = Math.ceil((xMax - base) / P) + 1;
  const out = [];

  for (let n = nMin; n <= nMax; n++) {
    const x = base + n * P;
    if (x < xMin || x > xMax) continue;

    // Keep parity tied to the absolute product index.
    // This prevents UP/DOWN assignment from swapping after phase wrapping.
    const flip = (n & 1) === 0;
    out.push({ bowlIndex: n, x, flip });
  }

  return out;
}

// Drop-in replacement for the old finite -12..3 drawing loop.
export function drawContinuousBowls(t, DATA, bowlWire) {
  const bowls = visibleBowlStates(t, DATA.params);
  for (const b of bowls) bowlWire(b.x, b.flip);
  return bowls;
}

// Suggested soak-test invariant.
export function assertPitchAndAlternation(bowls, pitch, tolerance = 1e-6) {
  const sorted = [...bowls].sort((a, b) => a.x - b.x);
  for (let i = 1; i < sorted.length; i++) {
    const dx = sorted[i].x - sorted[i - 1].x;
    if (Math.abs(dx - pitch) > tolerance) {
      throw new Error(`Pitch invariant failed: ${dx} != ${pitch}`);
    }
    if (sorted[i].flip === sorted[i - 1].flip) {
      throw new Error('Alternation invariant failed');
    }
  }
  return true;
}
