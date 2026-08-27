# Timing Screw Direction Correction – 2026-08-27

## User observation

The V13 kinematic viewer appeared to show the timing screw feeding in the wrong axial direction relative to the bowls.

That observation is correct for the sign convention used in the viewer.

## Helix equation used by the old viewer

The rendered helix was:

`phi(x,t) = 2*pi*x/P + omega*t`

For a constant phase / visible crest location:

`d(phi)/dt = 0`

therefore:

`(2*pi/P) dx/dt + omega = 0`

so:

`dx/dt = -P*omega/(2*pi)`

Thus the visible helical crest propagates toward **-X** when `omega > 0`.

The bowls, however, move toward **+X**.

## Correct viewer relation for current handedness

Keep the current helix handedness and reverse the screw phase sign:

`phi(x,t) = 2*pi*x/P - omega*t`

Then:

`dx/dt = +P*omega/(2*pi)`

At the baseline:

- pitch P = 160 mm
- screw speed = 160 rpm

therefore the axial phase-feed speed is:

`160 * 160 / 60 = 426.667 mm/s`

which is exactly the product speed at 160 bowls/min.

## Engineering invariant

For the current viewer coordinate/handedness convention:

- product transport = +X
- visible screw feed = +X
- use `phi = 2*pi*x/P - omega*t`

Do not change this sign independently from the screw handedness. If future CAD changes to the opposite helix handedness, rotation sign and feed direction must be solved together.

## Scope

This corrects the displayed screw kinematics and feed-direction convention. It does **not** by itself validate the regenerated V13 screw solid, groove/contact profile, torque, friction, or structural loads.
