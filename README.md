# Semiconductor Test Support Lab

This project simulates a basic Application Support Engineering environment inspired by semiconductor test automation workflows.

The goal of this lab is to practice Linux administration, Git/GitHub, Python scripting, CI/CD concepts, Jenkins pipeline execution, PostgreSQL integration, SQL metrics validation, Nginx dashboard publishing, troubleshooting, and technical documentation.

This project starts with simulated semiconductor test data and evolves into a more complete internal support workflow using Jenkins, PostgreSQL, Nginx, and Scrum-inspired practices.

## Project Purpose

In engineering environments, internal tools are often used to automate testing, collect results, store metrics, publish dashboards, and help teams identify failures quickly.

This lab simulates a simplified version of that workflow:

```text
Windows Workstation
   ↓ SSH / Git / Browser
Ubuntu Server VM
   ↓
GitHub Repository
   ↓
Jenkins Pipeline
   ↓
Python Test Simulator
   ↓
CSV Report
   ↓
PostgreSQL Database
   ↓
SQL Metrics Validation
   ↓
Python Dashboard Generator
   ↓
Nginx Dashboard
```

## Agile Scrum-Inspired Workflow

This project is organized using Scrum-inspired practices to simulate how technical work is delivered in an engineering environment.

The lab is divided into implementation sprints, each with a clear goal, deliverables, validation steps, documentation, and lessons learned.

Current sprint structure:

* Sprint 1: Ubuntu Server, SSH, Git, GitHub, and Python test simulation.
* Sprint 2: Jenkins CI/CD pipeline execution.
* Sprint 3: PostgreSQL integration and SQL metrics validation.
* Sprint 4: Nginx dashboard generated from PostgreSQL metrics.
* Sprint 5: Monitoring and additional troubleshooting documentation.
* Sprint 6: STDF-related semiconductor test data concepts.

More details are available in:

[Agile Scrum-Inspired Process](docs/agile-scrum-process.md)

## Current Features

* Ubuntu Server VM configured.
* SSH access enabled from Windows.
* Git and GitHub configured.
* Python test simulation script created.
* Simulated ASIC/FPGA test results generated.
* CSV report generated with PASS/FAIL results.
* Basic performance benchmarking included.
* Jenkins installed and configured.
* Jenkins pipeline created using a `Jenkinsfile`.
* Jenkins build executed successfully.
* Jenkins Credentials used to protect the PostgreSQL password.
* CSV report archived as a Jenkins build artifact.
* PostgreSQL installed and configured.
* Database `semiconductor_lab` created.
* Table `test_results` created for storing test execution data.
* CSV report imported automatically into PostgreSQL from Jenkins.
* SQL metrics queries created for total records, PASS/FAIL count, average duration, slowest test, and failed test details.
* Nginx installed and configured.
* Dashboard served through Nginx on port `8081`.
* Dashboard generated from PostgreSQL metrics using Python.
* Jenkins pipeline generates and validates the Nginx dashboard automatically.
* Technical documentation created for troubleshooting, Jenkins, PostgreSQL, Nginx dashboard automation, and Scrum-inspired workflow.

## Technologies Used

* Ubuntu Server
* Windows PowerShell
* SSH
* Git
* GitHub
* Python
* CSV reporting
* Jenkins
* Jenkins Credentials
* CI/CD pipeline concepts
* PostgreSQL
* SQL
* Database validation
* Nginx
* HTML
* Linux file permissions
* Markdown technical documentation

## Technologies Planned

* Application monitoring
* Additional troubleshooting scenarios
* STDF / semiconductor test data concepts

## Project Structure

```text
semiconductor-test-support-lab/
│
├── app/
│   ├── fake_chip_test.py
│   └── generate_dashboard.py
│
├── dashboard/
│   └── index.html
│
├── docs/
│   ├── agile-scrum-process.md
│   ├── incident-001-ubuntu-network-dhcp-netplan.md
│   ├── incident-002-jenkins-missing-postgresql-credential.md
│   ├── incident-003-jenkins-nginx-permission-denied.md
│   ├── jenkins-pipeline.md
│   ├── jenkins-postgresql-automation.md
│   └── postgresql-integration.md
│
├── reports/
│   └── test_results.csv
│
├── sql/
│   ├── create_test_results_table.sql
│   └── metrics_queries.sql
│
├── Jenkinsfile
├── .gitignore
└── README.md
```

## Python Test Simulator

The current Python script simulates test execution for different semiconductor-related components, including ASICs and FPGAs.

Script:

```text
app/fake_chip_test.py
```

Example simulated devices:

```text
ASIC-1001
ASIC-1002
FPGA-2001
FPGA-2002
CTRL-3001
```

Example simulated tests:

```text
Voltage Test
Frequency Test
Memory Test
Temperature Test
Signal Integrity Test
```

Each test generates:

* Timestamp
* Device ID
* Test name
* PASS/FAIL status
* Test duration in seconds

## Performance Benchmarking

The script includes basic performance benchmarking by measuring:

* Individual test execution time
* Total pipeline execution time
* Average test duration
* Slowest test
* Pass rate
* Fail count

Example output:

```text
===== Semiconductor Test Summary =====
Total tests executed: 25
Passed: 22
Failed: 3
Pass rate: 88.0%
Average test duration: 0.659 seconds
Report generated at: reports/test_results.csv
```

## Jenkins Pipeline

This project includes a Jenkins pipeline that automatically runs the Python semiconductor test simulator.

Pipeline flow:

```text
GitHub Repository
   ↓
Jenkins Pipeline
   ↓
Jenkinsfile
   ↓
Python Test Simulator
   ↓
CSV Report
   ↓
PostgreSQL Import
   ↓
SQL Metrics Validation
   ↓
Nginx Dashboard Generation
   ↓
Archived Build Artifacts
```

The pipeline performs the following actions:

* Pulls the project from GitHub.
* Reads the `Jenkinsfile`.
* Verifies that Python is available.
* Runs the semiconductor test simulation script.
* Displays the generated CSV report in the Jenkins console output.
* Imports the CSV report into PostgreSQL.
* Runs SQL metrics validation.
* Generates the Nginx dashboard from PostgreSQL metrics.
* Validates that the dashboard file exists.
* Archives the CSV report and dashboard HTML as build artifacts.

More details are available in:

[Jenkins Pipeline Documentation](docs/jenkins-pipeline.md)

[Jenkins PostgreSQL Automation Documentation](docs/jenkins-postgresql-automation.md)

## Jenkins Credentials

The PostgreSQL password is managed using Jenkins Credentials instead of being stored directly in the `Jenkinsfile`.

Credential ID used by the pipeline:

```text
postgres-lab-password
```

This allows Jenkins to inject the password securely during pipeline execution.

In the Jenkins console output, the password is masked:

```text
PGPASSWORD=****
```

This demonstrates a better CI/CD security practice by avoiding plain-text secrets in source control.

## PostgreSQL Integration

This project uses PostgreSQL to store semiconductor test simulation results generated by the Python script.

Originally, the Python simulator generated a CSV report. PostgreSQL was added to store that data in a relational database and allow SQL-based validation and metrics analysis.

Database created:

```text
semiconductor_lab
```

Main table:

```text
test_results
```

The table stores:

* Timestamp
* Device ID
* Test name
* PASS/FAIL status
* Test duration in seconds
* Record creation timestamp

SQL scripts are available in:

```text
sql/create_test_results_table.sql
sql/metrics_queries.sql
```

More details are available in:

[PostgreSQL Integration Documentation](docs/postgresql-integration.md)

## SQL Metrics Validation

After importing the CSV report into PostgreSQL, SQL queries are used to validate the test data.

Example validation results:

```text
Total records: 25
PASS: 22
FAIL: 3
Average duration: 0.659 seconds
```

Example queries include:

```sql
SELECT COUNT(*) FROM test_results;
```

```sql
SELECT status, COUNT(*)
FROM test_results
GROUP BY status;
```

```sql
SELECT ROUND(AVG(duration_seconds), 3) AS average_duration
FROM test_results;
```

## Nginx Dashboard

This project includes an Nginx-hosted dashboard generated from PostgreSQL metrics.

Dashboard URL in the local lab environment:

```text
http://192.168.159.135:8081
```

Dashboard generation script:

```text
app/generate_dashboard.py
```

The script reads metrics from PostgreSQL and generates an HTML dashboard.

The dashboard displays:

* Jenkins pipeline status.
* Total test records.
* PASS count.
* FAIL count.
* Average test duration.
* Slowest test.
* Failed test details.
* Current architecture.

The generated dashboard is published to:

```text
/var/www/semiconductor-dashboard/index.html
```

The dashboard is served by Nginx on port:

```text
8081
```

## How to Run the Script Manually

From the project root directory, run:

```bash
python3 app/fake_chip_test.py
```

After execution, the script generates a CSV report:

```text
reports/test_results.csv
```

To view the report:

```bash
cat reports/test_results.csv
```

## How to Run SQL Metrics

To execute the metrics queries against PostgreSQL:

```bash
PGPASSWORD='lab_password' psql -h localhost -U lab_user -d semiconductor_lab -f sql/metrics_queries.sql
```

This runs the SQL validation queries stored in:

```text
sql/metrics_queries.sql
```

## How to Generate the Dashboard Manually

To generate the dashboard manually from PostgreSQL metrics:

```bash
DB_PASSWORD='lab_password' python3 app/generate_dashboard.py
```

This generates:

```text
dashboard/index.html
/var/www/semiconductor-dashboard/index.html
```

The dashboard can then be viewed at:

```text
http://192.168.159.135:8081
```

## Troubleshooting Documentation

This project includes incident documentation based on real issues encountered during the lab.

Current incident reports:

* [Incident 001: Ubuntu Server VM Network Issue - DHCP and Netplan](docs/incident-001-ubuntu-network-dhcp-netplan.md)
* [Incident 002: Jenkins Pipeline Failed Due to Missing PostgreSQL Credential](docs/incident-002-jenkins-missing-postgresql-credential.md)
* [Incident 003: Jenkins Failed to Generate Nginx Dashboard Due to Linux File Permissions](docs/incident-003-jenkins-nginx-permission-denied.md)

These documents include:

* Summary
* Environment
* Issue
* Investigation
* Root cause
* Resolution
* Validation
* Lessons learned
* Application Support relevance

## Why This Lab Matters

This lab is designed to practice skills commonly used in Application Support Engineering environments:

* Supporting Linux-based tools.
* Working from a Windows workstation.
* Using SSH for remote access.
* Managing code with Git and GitHub.
* Automating technical workflows.
* Running Jenkins CI/CD pipelines.
* Managing credentials securely in Jenkins.
* Generating and reviewing test reports.
* Storing application-generated data in PostgreSQL.
* Running SQL queries for validation and metrics.
* Publishing dashboards with Nginx.
* Troubleshooting Linux permissions.
* Understanding performance metrics.
* Preparing for CI/CD pipeline support.
* Documenting troubleshooting scenarios.
* Working with Scrum-inspired project structure.

## Application Support Relevance

This project demonstrates a simplified version of workflows that an Application Support Engineer may support in a real engineering environment.

It includes:

* Linux server administration.
* Windows-to-Linux remote access.
* GitHub-based source control.
* Jenkins pipeline execution.
* Jenkins credential usage.
* Python-based automation.
* CSV report generation.
* PostgreSQL data storage.
* SQL metrics validation.
* Nginx dashboard publishing.
* Linux file permission troubleshooting.
* Technical documentation.
* Incident documentation.
* Incremental delivery using Scrum-inspired practices.

In a real environment, similar workflows may be used to support internal engineering tools, automated test systems, build pipelines, performance reporting, operational dashboards, and troubleshooting processes.

## Future Improvements

Planned next steps:

1. Add monitoring checks for Jenkins, PostgreSQL, and Nginx services.
2. Add additional troubleshooting documentation for service failures.
3. Explore STDF-related concepts for semiconductor test data processing.
4. Improve dashboard styling and add more metrics.
5. Add automated health-check scripts.

## Learning Goal

The main goal of this project is not to perform real semiconductor testing, but to simulate the type of technical workflow an Application Support Engineer might support in an engineering environment.

This includes automation, pipeline execution, data validation, monitoring, troubleshooting, SQL metrics, dashboard publishing, and technical documentation.
