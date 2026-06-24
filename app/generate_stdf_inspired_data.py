import csv
import random
from datetime import datetime, timedelta
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "data" / "stdf_inspired_test_records.csv"

random.seed(2026)


TEST_SPECS = [
    {
        "test_number": 1001,
        "test_name": "Voltage Test",
        "unit": "V",
        "low_limit": 0.95,
        "high_limit": 1.05,
        "target": 1.00,
        "sigma": 0.030,
    },
    {
        "test_number": 1002,
        "test_name": "Frequency Test",
        "unit": "MHz",
        "low_limit": 450.0,
        "high_limit": 550.0,
        "target": 500.0,
        "sigma": 28.0,
    },
    {
        "test_number": 1003,
        "test_name": "Memory BIST",
        "unit": "%",
        "low_limit": 95.0,
        "high_limit": 100.0,
        "target": 98.5,
        "sigma": 1.4,
    },
    {
        "test_number": 1004,
        "test_name": "Leakage Current",
        "unit": "mA",
        "low_limit": 0.0,
        "high_limit": 2.50,
        "target": 1.20,
        "sigma": 0.45,
    },
    {
        "test_number": 1005,
        "test_name": "Temperature Test",
        "unit": "C",
        "low_limit": 20.0,
        "high_limit": 85.0,
        "target": 45.0,
        "sigma": 14.0,
    },
    {
        "test_number": 1006,
        "test_name": "Signal Integrity",
        "unit": "ns",
        "low_limit": 0.0,
        "high_limit": 0.35,
        "target": 0.18,
        "sigma": 0.07,
    },
]


LOTS = ["LOT-2026-001", "LOT-2026-002"]
WAFERS = ["WAFER-01", "WAFER-02", "WAFER-03"]
TESTERS = ["ATE-01", "ATE-02"]
DEVICE_TYPES = ["ASIC", "FPGA"]


def determine_result(measured_value: float, low_limit: float, high_limit: float) -> tuple[str, str]:
    if measured_value < low_limit:
        return "FAIL", "LOW_LIMIT"

    if measured_value > high_limit:
        return "FAIL", "HIGH_LIMIT"

    return "PASS", ""


def generate_measurement(spec: dict, wafer_id: str, site_id: int) -> float:
    measured_value = random.gauss(spec["target"], spec["sigma"])

    outlier_rate = 0.06

    if wafer_id == "WAFER-03":
        outlier_rate += 0.04

    if site_id == 3:
        outlier_rate += 0.05

    if random.random() < outlier_rate:
        direction = random.choice([-1, 1])
        measured_value += direction * spec["sigma"] * random.uniform(3.0, 5.0)

    return round(measured_value, 4)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    fieldnames = [
        "timestamp",
        "lot_id",
        "wafer_id",
        "x_coord",
        "y_coord",
        "site_id",
        "tester_id",
        "device_type",
        "device_id",
        "test_number",
        "test_name",
        "measurement_value",
        "low_limit",
        "high_limit",
        "unit",
        "result",
        "fail_reason",
    ]

    rows = []
    base_time = datetime.now().replace(microsecond=0)
    record_counter = 0

    for lot_id in LOTS:
        for wafer_id in WAFERS:
            for die_index in range(1, 11):
                x_coord = random.randint(1, 20)
                y_coord = random.randint(1, 20)
                site_id = ((die_index - 1) % 4) + 1
                tester_id = random.choice(TESTERS)
                device_type = random.choice(DEVICE_TYPES)
                device_id = f"{device_type}-{lot_id[-3:]}-{wafer_id[-2:]}-{die_index:03d}"

                for spec in TEST_SPECS:
                    record_counter += 1

                    measured_value = generate_measurement(spec, wafer_id, site_id)
                    result, fail_reason = determine_result(
                        measured_value,
                        spec["low_limit"],
                        spec["high_limit"],
                    )

                    timestamp = base_time + timedelta(seconds=record_counter)

                    rows.append(
                        {
                            "timestamp": timestamp.isoformat(),
                            "lot_id": lot_id,
                            "wafer_id": wafer_id,
                            "x_coord": x_coord,
                            "y_coord": y_coord,
                            "site_id": site_id,
                            "tester_id": tester_id,
                            "device_type": device_type,
                            "device_id": device_id,
                            "test_number": spec["test_number"],
                            "test_name": spec["test_name"],
                            "measurement_value": measured_value,
                            "low_limit": spec["low_limit"],
                            "high_limit": spec["high_limit"],
                            "unit": spec["unit"],
                            "result": result,
                            "fail_reason": fail_reason,
                        }
                    )

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    passed = sum(1 for row in rows if row["result"] == "PASS")
    failed = sum(1 for row in rows if row["result"] == "FAIL")
    total = len(rows)
    yield_percentage = round((passed / total) * 100, 2)

    print("===== STDF-Inspired Data Generation Summary =====")
    print(f"Output file: {OUTPUT_PATH.relative_to(PROJECT_ROOT)}")
    print(f"Total records generated: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Yield: {yield_percentage}%")


if __name__ == "__main__":
    main()
