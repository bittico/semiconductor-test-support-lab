import csv
import random
import time
from datetime import datetime
from pathlib import Path

devices = [
    "ASIC-1001",
    "ASIC-1002",
    "FPGA-2001",
    "FPGA-2002",
    "CTRL-3001"
]

tests = [
    "Voltage Test",
    "Frequency Test",
    "Memory Test",
    "Temperature Test",
    "Signal Integrity Test"
]

results = []

Path("reports").mkdir(exist_ok=True)

pipeline_start = time.perf_counter()

for device in devices:
    for test_name in tests:
        test_start = time.perf_counter()

        simulated_duration = random.uniform(0.2, 1.2)
        time.sleep(simulated_duration)

        status = random.choices(
            ["PASS", "FAIL"],
            weights=[85, 15],
            k=1
        )[0]

        test_end = time.perf_counter()
        test_duration = round(test_end - test_start, 3)

        results.append({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "device_id": device,
            "test_name": test_name,
            "status": status,
            "duration_seconds": test_duration
        })

pipeline_end = time.perf_counter()
total_pipeline_duration = round(pipeline_end - pipeline_start, 3)

report_path = "reports/test_results.csv"

with open(report_path, "w", newline="") as file:
    fieldnames = [
        "timestamp",
        "device_id",
        "test_name",
        "status",
        "duration_seconds"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

total_tests = len(results)
passed = sum(1 for r in results if r["status"] == "PASS")
failed = sum(1 for r in results if r["status"] == "FAIL")
average_duration = round(
    sum(r["duration_seconds"] for r in results) / total_tests,
    3
)

slowest_test = max(results, key=lambda r: r["duration_seconds"])

print("===== Semiconductor Test Summary =====")
print(f"Total tests executed: {total_tests}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Pass rate: {round((passed / total_tests) * 100, 2)}%")
print(f"Average test duration: {average_duration} seconds")
print(f"Slowest test: {slowest_test['test_name']} on {slowest_test['device_id']} - {slowest_test['duration_seconds']} seconds")
print(f"Total pipeline duration: {total_pipeline_duration} seconds")
print(f"Report generated at: {report_path}")
