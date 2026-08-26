#!/usr/bin/env python3
"""Repository-level sanity checks for the Bowl Inverter engineering baseline.

This script checks invariant timing formulas, corrected bowl geometry, and the
current flip-direction/trigger-role decisions. It intentionally does NOT claim
that historical V6/V10.10/V11 CAD is currently valid after the 2026-08-26
geometry and rotation-direction corrections.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def close(a: float, b: float, tol: float = 1e-3) -> bool:
    return abs(a - b) <= tol


def main() -> None:
    baseline = read_json("data/current_baseline.json")

    product = baseline["product"]
    require(close(float(product["bottom_diameter_mm"]), 138.0),
            "corrected conveyor-contact bottom diameter must be 138 mm")
    require(close(float(product["top_diameter_mm"]), 120.0),
            "corrected top diameter must be 120 mm")
    require(close(float(product["height_mm"]), 62.0), "height must be 62 mm")

    taper = math.degrees(math.atan2((138.0 - 120.0) / 2.0, 62.0))
    require(close(taper, float(product["taper_half_angle_deg"]), 1e-5),
            "corrected taper half-angle mismatch")

    line = baseline["line"]
    rate = float(line["rate_bowls_per_min"])
    pitch = float(line["pitch_mm"])
    bowl_dt = 60.0 / rate
    line_speed = pitch / bowl_dt
    flip_dt = 2.0 * bowl_dt

    require(close(bowl_dt, float(line["bowl_interval_s"])), "bowl interval mismatch")
    require(close(flip_dt, float(line["flip_event_interval_s"])), "flip event interval mismatch")
    require(close(line_speed, float(line["axial_speed_mm_s"]), 1e-3), "line speed mismatch")

    timing = baseline["timing_relations"]
    screw_rpm = float(timing["single_start_screw_rpm_at_baseline"])
    rotor_rpm = float(timing["three_arm_rotor_rpm_at_baseline"])

    screw_deg_per_bowl = screw_rpm * 360.0 / 60.0 * bowl_dt
    rotor_deg_per_bowl = rotor_rpm * 360.0 / 60.0 * bowl_dt
    rotor_deg_per_flip = rotor_deg_per_bowl * 2.0

    require(close(screw_deg_per_bowl, 360.0), "single-start screw must rotate 360 deg per bowl")
    require(close(rotor_deg_per_bowl, 60.0), "3-arm rotor must rotate 60 deg per bowl")
    require(close(rotor_deg_per_flip, 120.0), "3-arm rotor must rotate 120 deg per flip event")

    # The corrected product geometry invalidated the previous CAD/contact PASS.
    gv = baseline["geometry_validation"]
    require(gv["status"] == "REVALIDATION_REQUIRED",
            "geometry must remain REVALIDATION_REQUIRED until a new corrected-geometry checkpoint is created")
    require(gv["old_geometry_pass_claims_current"] is False,
            "historical V6/V10.10/V11 geometry PASS must not be treated as current")
    require(float(gv["diagnostic_old_return_path_min_shaft_clearance_mm"]) < 5.0,
            "diagnostic should record why the old RETURN path was invalidated")
    require(float(gv["diagnostic_old_flip_path_min_shaft_clearance_mm"]) < 5.0,
            "diagnostic should record why the old FLIP path was invalidated")

    # Rotation direction and transfer-actuator role corrected after user review.
    rotation = baseline["rotation_direction"]
    require(rotation["viewer_expected_selected_flip"] == "counter_clockwise",
            "selected bowl viewer direction must remain counter-clockwise until V13 proves otherwise")
    require("stale" in rotation["old_positive_52_to_180_branch_status"],
            "old positive 52->180 angular branch must remain marked stale")

    actuator = baseline["transfer_actuator"]
    require(actuator["new_role"] == "brief_tangent_trigger_not_continuous_flipping_paddle",
            "selected actuator must remain a brief trigger, not a continuous flipping paddle")
    require(actuator["no_free_flight"] is True, "selected bowl must not use uncontrolled free flight")

    print("PASS: corrected baseline timing/geometry/direction metadata sanity checks")
    print("  bottom / top diameter  : 138 / 120 mm")
    print(f"  taper half-angle       : {taper:.3f} deg")
    print(f"  bowl interval          : {bowl_dt:.3f} s")
    print(f"  line speed             : {line_speed:.3f} mm/s")
    print(f"  screw deg / bowl       : {screw_deg_per_bowl:.1f}")
    print(f"  rotor deg / bowl       : {rotor_deg_per_bowl:.1f}")
    print(f"  rotor deg / flip event : {rotor_deg_per_flip:.1f}")
    print("  selected flip viewer   : counter-clockwise")
    print("  transfer actuator role : brief tangent trigger")
    print("STATUS: timing relations PASS; mechanical geometry/force trajectory REVALIDATION REQUIRED")
    print("NOTE: do not use historical V11/V10.10 clearance/contact PASS as current design evidence.")


if __name__ == "__main__":
    main()
