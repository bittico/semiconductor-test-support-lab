import os
import socket
import subprocess
import urllib.request
from datetime import datetime
from pathlib import Path


REPORT_PATH = Path("reports/health_check_report.txt")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "semiconductor_lab")
DB_USER = os.getenv("DB_USER", "lab_user")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def check_service(service_name: str) -> tuple[bool, str]:
    result = subprocess.run(
        ["systemctl", "is-active", service_name],
        capture_output=True,
        text=True
    )

    status = result.stdout.strip()

    if status == "active":
        return True, f"{service_name}: active"

    return False, f"{service_name}: {status or 'not active'}"


def check_port(host: str, port: int, name: str) -> tuple[bool, str]:
    try:
        with socket.create_connection((host, port), timeout=3):
            return True, f"{name} port {port}: reachable"
    except OSError as error:
        return False, f"{name} port {port}: not reachable - {error}"


def check_http(url: str, name: str) -> tuple[bool, str]:
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            status_code = response.status
            if status_code == 200:
                return True, f"{name}: HTTP {status_code}"
            return False, f"{name}: HTTP {status_code}"
    except Exception as error:
        return False, f"{name}: failed - {error}"


def check_database_records() -> tuple[bool, str]:
    if not DB_PASSWORD:
        return False, "PostgreSQL data check: DB_PASSWORD is missing"

    env = os.environ.copy()
    env["PGPASSWORD"] = DB_PASSWORD

    command = [
        "psql",
        "-h", DB_HOST,
        "-U", DB_USER,
        "-d", DB_NAME,
        "-t",
        "-A",
        "-c", "SELECT COUNT(*) FROM test_results;"
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            env=env,
            check=True
        )

        count = result.stdout.strip()

        if count == "25":
            return True, f"PostgreSQL data check: {count} records found"

        return False, f"PostgreSQL data check: expected 25 records, found {count}"

    except subprocess.CalledProcessError as error:
        return False, f"PostgreSQL data check failed: {error.stderr.strip()}"


def main() -> None:
    checks = [
        check_service("jenkins"),
        check_service("postgresql"),
        check_service("nginx"),
        check_port("localhost", 8080, "Jenkins"),
        check_port("localhost", 5432, "PostgreSQL"),
        check_port("localhost", 8081, "Nginx Dashboard"),
        check_http("http://localhost:8081", "Nginx Dashboard HTTP"),
        check_database_records(),
    ]

    passed = sum(1 for status, _ in checks if status)
    failed = len(checks) - passed

    lines = [
        "===== Application Support Health Check Report =====",
        f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"Total checks: {len(checks)}",
        f"Passed: {passed}",
        f"Failed: {failed}",
        "",
        "Details:"
    ]

    for status, message in checks:
        prefix = "PASS" if status else "FAIL"
        lines.append(f"[{prefix}] {message}")

    REPORT_PATH.parent.mkdir(exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines))

    if failed > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
