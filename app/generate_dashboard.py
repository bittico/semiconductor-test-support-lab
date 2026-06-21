import os
import subprocess
from datetime import datetime
from pathlib import Path


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "semiconductor_lab")
DB_USER = os.getenv("DB_USER", "lab_user")
DB_PASSWORD = os.getenv("DB_PASSWORD")

REPO_DASHBOARD_PATH = Path("dashboard/index.html")
NGINX_DASHBOARD_PATH = Path("/var/www/semiconductor-dashboard/index.html")


def run_query(query: str) -> str:
    if not DB_PASSWORD:
        raise SystemExit("ERROR: DB_PASSWORD environment variable is required.")

    env = os.environ.copy()
    env["PGPASSWORD"] = DB_PASSWORD

    command = [
        "psql",
        "-h", DB_HOST,
        "-U", DB_USER,
        "-d", DB_NAME,
        "-t",
        "-A",
        "-c", query
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        env=env,
        check=True
    )

    return result.stdout.strip()


def run_table_query(query: str) -> list[str]:
    if not DB_PASSWORD:
        raise SystemExit("ERROR: DB_PASSWORD environment variable is required.")

    env = os.environ.copy()
    env["PGPASSWORD"] = DB_PASSWORD

    command = [
        "psql",
        "-h", DB_HOST,
        "-U", DB_USER,
        "-d", DB_NAME,
        "-t",
        "-A",
        "-F", "|",
        "-c", query
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        env=env,
        check=True
    )

    output = result.stdout.strip()

    if not output:
        return []

    return output.splitlines()


def main() -> None:
    total_records = run_query("SELECT COUNT(*) FROM test_results;")
    pass_count = run_query("SELECT COUNT(*) FROM test_results WHERE status = 'PASS';")
    fail_count = run_query("SELECT COUNT(*) FROM test_results WHERE status = 'FAIL';")

    average_duration = run_query(
        "SELECT COALESCE(ROUND(AVG(duration_seconds), 3), 0) FROM test_results;"
    )

    slowest_test = run_query(
        """
        SELECT device_id || ' - ' || test_name || ' - ' || status || ' - ' || duration_seconds || ' seconds'
        FROM test_results
        ORDER BY duration_seconds DESC
        LIMIT 1;
        """
    )

    failed_tests = run_table_query(
        """
        SELECT device_id, test_name, duration_seconds
        FROM test_results
        WHERE status = 'FAIL'
        ORDER BY timestamp;
        """
    )

    failed_rows_html = ""

    if failed_tests:
        for row in failed_tests:
            device_id, test_name, duration = row.split("|")
            failed_rows_html += f"""
            <tr>
                <td>{device_id}</td>
                <td>{test_name}</td>
                <td>{duration}</td>
            </tr>
            """
    else:
        failed_rows_html = """
            <tr>
                <td colspan="3">No failed tests found.</td>
            </tr>
        """

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Semiconductor Test Support Dashboard</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f6f8;
            color: #222;
        }}

        h1 {{
            color: #1f2937;
        }}

        .card {{
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            border: 1px solid #ddd;
        }}

        .metric {{
            font-size: 28px;
            font-weight: bold;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}

        th {{
            background-color: #f0f2f5;
        }}

        .success {{
            color: green;
        }}

        .fail {{
            color: #b91c1c;
        }}

        .footer {{
            font-size: 12px;
            color: #666;
        }}
    </style>
</head>
<body>
    <h1>Semiconductor Test Support Dashboard</h1>

    <div class="card">
        <h2>Pipeline Status</h2>
        <p class="metric success">Jenkins Pipeline: SUCCESS</p>
    </div>

    <div class="card">
        <h2>Latest Test Metrics from PostgreSQL</h2>
        <p>Total Records: <strong>{total_records}</strong></p>
        <p>PASS: <strong class="success">{pass_count}</strong></p>
        <p>FAIL: <strong class="fail">{fail_count}</strong></p>
        <p>Average Duration: <strong>{average_duration}</strong> seconds</p>
        <p>Slowest Test: <strong>{slowest_test}</strong></p>
    </div>

    <div class="card">
        <h2>Failed Test Details</h2>
        <table>
            <thead>
                <tr>
                    <th>Device ID</th>
                    <th>Test Name</th>
                    <th>Duration Seconds</th>
                </tr>
            </thead>
            <tbody>
                {failed_rows_html}
            </tbody>
        </table>
    </div>

    <div class="card">
        <h2>Current Architecture</h2>
        <p>GitHub &rarr; Jenkins &rarr; Python &rarr; CSV &rarr; PostgreSQL &rarr; SQL Metrics &rarr; Nginx Dashboard</p>
    </div>

    <p class="footer">Dashboard generated at: {generated_at}</p>
</body>
</html>
"""

    REPO_DASHBOARD_PATH.parent.mkdir(exist_ok=True)
    REPO_DASHBOARD_PATH.write_text(html_content, encoding="utf-8")
    NGINX_DASHBOARD_PATH.write_text(html_content, encoding="utf-8")

    print("Dashboard generated successfully.")
    print(f"Repository copy: {REPO_DASHBOARD_PATH}")
    print(f"Nginx copy: {NGINX_DASHBOARD_PATH}")


if __name__ == "__main__":
    main()
