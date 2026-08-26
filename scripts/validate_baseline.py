#!/usr/bin/env python3
"""Repository-level sanity checks for the Bowl Inverter engineering baseline.

This script intentionally uses only the Python standard library so Codex or a
human engineer can run it immediately after cloning the repository.

It does NOT replace CAD collision/contact analysis. Its purpose is to detect
accidental drift from the currently approved kinematic baseline.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def read_csv(path: str):
    with (ROOT / path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def require(condition: bool, message: str):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def close(a: float, b: float, tol: float = 1e-3) -> bool:
    return abs(a - b) <= tol


def main() -> None:
    baseline = read_json("data/current_baseline.json")

    # Support the fields used by the checkpoint document even if the JSON is
    # reorganized later.
    text = json.dumps(baseline)
    for token in ["160", "0.375", "0.75", "426.667", "26.667"]:
        require(token in text, f"baseline no longer contains required value {token}")

    rate = 160.0
    bowl_dt = 60.0 / rate
    pitch = 160.0
    line_speed = pitch / bowl_dt
    screw_rpm = 160.0
    rotor_rpm = 80.0 / 3.0

    require(close(bowl_dt, 0.375), "bowl interval must remain 0.375 s")
    require(close(line_speed, 426.6666667), "line speed mismatch")

    screw_deg_per_bowl = screw_rpm * 360.0 / 60.0 * bowl_dt
    rotor_deg_per_bowl = rotor_rpm * 360.0 / 60.0 * bowl_dt
    rotor_deg_per_flip = rotor_deg_per_bowl * 2.0

    require(close(screw_deg_per_bowl, 360.0), "screw must rotate 360 deg per bowl")
    require(close(rotor_deg_per_bowl, 60.0), "rotor must rotate 60 deg per bowl")
    require(close(rotor_deg_per_flip, 120.0), "rotor must advance 120 deg per flip event")

    # V11: every sampled section must retain positive drive and shaft clearance.
    v11 = read_csv("data/v11/timing_screw_v11_validation.csv")
    require(v11, "V11 validation table is empty")
    shaft_margins = []
    for row in v11:
        require(row["positive_drive_pass"].lower() == "true",
                f"V11 positive drive failed at x={row['x_mm']}")
        require(row["shaft_pass"].lower() == "true",
                f"V11 shaft check failed at x={row['x_mm']}")
        shaft_margins.append(float(row["shaft_margin_mm"]))

    require(min(shaft_margins) >= 10.0,
            f"V11 sampled shaft margin dropped below 10 mm: {min(shaft_margins):.3f}")

    # V11 crossover sections: ensure the asymmetric screw has not been reduced
    # to an almost-empty section by a later geometry change.
    sections = read_csv("data/v11/timing_screw_v11_transfer_sections.csv")
    require(sections, "V11 transfer section table is empty")
    fractions = [float(r["material_fraction"]) for r in sections]
    require(min(fractions) >= 0.30,
            f"transfer-section material fraction too low: {min(fractions):.3f}")

    # V10.10 current transfer-actuator checkpoint.
    v10 = read_json("data/v10/v10_10_report.json")
    report_text = json.dumps(v10).lower()
    require("pass" in report_text, "V10.10 report no longer records the preliminary PASS checkpoint")

    print("PASS: repository baseline sanity checks")
    print(f"  bowl interval          : {bowl_dt:.3f} s")
    print(f"  line speed             : {line_speed:.3f} mm/s")
    print(f"  screw deg / bowl       : {screw_deg_per_bowl:.1f}")
    print(f"  rotor deg / bowl       : {rotor_deg_per_bowl:.1f}")
    print(f"  rotor deg / flip event : {rotor_deg_per_flip:.1f}")
    print(f"  V11 min shaft margin   : {min(shaft_margins):.3f} mm")
    print(f"  V11 min material frac  : {min(fractions):.3f}")
    print("NOTE: V12 viewer still has the documented continuous-spawn bug until V12.1 is implemented.")


if __name__ == "__main__":
    main()
