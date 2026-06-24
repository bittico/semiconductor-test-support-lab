import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

INPUT_PATH = PROJECT_ROOT / "data" / "stdf_inspired_test_records.csv"
SUMMARY_PATH = PROJECT_ROOT / "reports" / "stdf_yield_summary.csv"
BREAKDOWN_PATH = PROJECT_ROOT / "reports" / "stdf_yield_breakdown.csv"
REPORT_PATH = PROJECT_ROOT / "reports" / "stdf_yield_report.txt"


def new_stats() -> dict:
    return {
        "total": 0,
        "passed": 0,
        "failed": 0,
    }


def update_stats(stats: dict, result: str) -> None:
    stats["total"] += 1

    if result == "PASS":
        stats["passed"] += 1
    elif result == "FAIL":
        stats["failed"] += 1


def calculate_yield(passed: int, total: int) -> float:
    if total == 0:
        return 0.0

    return round((passed / total) * 100, 2)


def read_records() -> list[dict]:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

    with INPUT_PATH.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_summary(total_stats: dict) -> None:
    SUMMARY_PATH.parent.mkdir(exist_ok=True)

    yield_percentage = calculate_yield(
        total_stats["passed"],
        total_stats["total"],
    )

    rows = [
        {"metric": "total_records", "value": total_stats["total"]},
        {"metric": "passed", "value": total_stats["passed"]},
        {"metric": "failed", "value": total_stats["failed"]},
        {"metric": "yield_percentage", "value": yield_percentage},
    ]

    with SUMMARY_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["metric", "value"])
        writer.writeheader()
        writer.writerows(rows)


def write_breakdown(category_stats: dict[str, dict[str, dict]]) -> None:
    BREAKDOWN_PATH.parent.mkdir(exist_ok=True)

    fieldnames = [
        "category",
        "name",
        "total",
        "passed",
        "failed",
        "yield_percentage",
    ]

    with BREAKDOWN_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for category, values in category_stats.items():
            for name, stats in sorted(values.items()):
                writer.writerow(
                    {
                        "category": category,
                        "name": name,
                        "total": stats["total"],
                        "passed": stats["passed"],
                        "failed": stats["failed"],
                        "yield_percentage": calculate_yield(
                            stats["passed"],
                            stats["total"],
                        ),
                    }
                )


def build_report(total_stats: dict, category_stats: dict[str, dict[str, dict]]) -> str:
    lines = []

    yield_percentage = calculate_yield(
        total_stats["passed"],
        total_stats["total"],
    )

    lines.append("===== STDF-Inspired Yield Report =====")
    lines.append(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("Overall Summary")
    lines.append(f"Total records: {total_stats['total']}")
    lines.append(f"Passed: {total_stats['passed']}")
    lines.append(f"Failed: {total_stats['failed']}")
    lines.append(f"Yield: {yield_percentage}%")
    lines.append("")

    for category, values in category_stats.items():
        lines.append(f"{category.replace('_', ' ').title()} Breakdown")

        for name, stats in sorted(values.items()):
            category_yield = calculate_yield(
                stats["passed"],
                stats["total"],
            )

            lines.append(
                f"- {name}: total={stats['total']}, "
                f"passed={stats['passed']}, "
                f"failed={stats['failed']}, "
                f"yield={category_yield}%"
            )

        lines.append("")

    return "\n".join(lines)


def main() -> None:
    records = read_records()

    total_stats = new_stats()

    category_stats = {
        "lot_id": defaultdict(new_stats),
        "wafer_id": defaultdict(new_stats),
        "site_id": defaultdict(new_stats),
        "tester_id": defaultdict(new_stats),
        "device_type": defaultdict(new_stats),
        "test_name": defaultdict(new_stats),
        "fail_reason": defaultdict(new_stats),
    }

    for record in records:
        result = record["result"]

        update_stats(total_stats, result)

        update_stats(category_stats["lot_id"][record["lot_id"]], result)
        update_stats(category_stats["wafer_id"][record["wafer_id"]], result)
        update_stats(category_stats["site_id"][record["site_id"]], result)
        update_stats(category_stats["tester_id"][record["tester_id"]], result)
        update_stats(category_stats["device_type"][record["device_type"]], result)
        update_stats(category_stats["test_name"][record["test_name"]], result)

        fail_reason = record["fail_reason"] if record["fail_reason"] else "NONE"
        update_stats(category_stats["fail_reason"][fail_reason], result)

    write_summary(total_stats)
    write_breakdown(category_stats)

    report = build_report(total_stats, category_stats)
    REPORT_PATH.write_text(report + "\n", encoding="utf-8")

    print(report)
    print(f"Summary CSV generated at: {SUMMARY_PATH.relative_to(PROJECT_ROOT)}")
    print(f"Breakdown CSV generated at: {BREAKDOWN_PATH.relative_to(PROJECT_ROOT)}")
    print(f"Text report generated at: {REPORT_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
