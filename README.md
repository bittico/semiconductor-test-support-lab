# Semiconductor Test Support Lab

## Overview

This project simulates an Application Support Engineering environment inspired by semiconductor test automation workflows.

The lab demonstrates how an internal engineering support toolchain can execute test simulations, generate reports, store results in a database, validate metrics, publish a dashboard, and run health checks through a CI/CD pipeline.

The main goal is not to perform real semiconductor testing, but to practice the type of technical workflow an Application Support Engineer may support in an engineering environment.

## Current Project Status

| Sprint   | Focus Area                                          | Status    |
| -------- | --------------------------------------------------- | --------- |
| Sprint 1 | Linux, SSH, GitHub, and Python test simulation      | Completed |
| Sprint 2 | Jenkins CI/CD pipeline                              | Completed |
| Sprint 3 | PostgreSQL integration and SQL metrics validation   | Completed |
| Sprint 4 | Nginx dashboard generated from PostgreSQL metrics   | Completed |
| Sprint 5 | Application health checks and monitoring validation | Completed |
| Sprint 6 | STDF-related semiconductor test data concepts       | Planned   |

## Architecture

```text
Windows Workstation
   ↓ SSH / Browser
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
   ↓
Application Health Checks
   ↓
Archived Jenkins Artifacts
```

## Project Purpose

In engineering environments, internal tools are often used to automate testing, collect results, store metrics, publish dashboards, and help teams identify failures quickly.

This lab simulates a simplified version of that workflow by combining:

* Linux administration
* Git and GitHub
* Python automation
* Jenkins CI/CD pipelines
* PostgreSQL data storage
* SQL metrics validation
* Nginx dashboard publishing
* Application health checks
* Troubleshooting documentation
* Scrum-inspired project organization

## Current Features

* Ubuntu Server VM configured.
* SSH access enabled from Windows.
* Git and GitHub repository configured.
* Python semiconductor test simulator created.
* Simulated ASIC and FPGA test results generated.
* CSV report generated with PASS/FAIL results.
* Basic performance benchmarking included.
* Jenkins installed and configured.
* Jenkins pipeline created using a `Jenkinsfile`.
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
* Application health check script created.
* Jenkins pipeline validates services, ports, HTTP response, and database records.
* Health check report generated and archived as a Jenkins build artifact.
* Troubleshooting incidents documented using root cause analysis format.

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
* Nginx
* HTML
* Linux file permissions
* Service health checks
* Port connectivity checks
* HTTP endpoint validation
* Markdown technical documentation

## Technologies Planned

* STDF / semiconductor test data concepts
* Additional troubleshooting scenarios
* Dashboard improvements
* Historical metrics
* Automated alerting concepts

## Repository Structure

```text
semiconductor-test-support-lab/
│
├── app/
│   ├── fake_chip_test.py
│   ├── generate_dashboard.py
│   └── health_check.py
│
├── dashboard/
│   └── index.html
│
├── docs/
│   ├── agile-scrum-process.md
│   ├── health-checks.md
│   ├── incident-001-ubuntu-network-dhcp-netplan.md
│   ├── incident-002-jenkins-missing-postgresql-credential.md
│   ├── incident-003-jenkins-nginx-permission-denied.md
│   ├── jenkins-pipeline.md
│   ├── jenkins-postgresql-automation.md
│   └── postgresql-integration.md
│
├── reports/
│   ├── test_results.csv
│   └── health_check_report.txt
│
├── sql/
│   ├── create_test_results_table.sql
│   └── metrics_queries.sql
│
├── Jenkinsfile
├── .gitignore
└── README.md
```

## Scrum-Inspired Workflow

This project is organized using Scrum-inspired practices to simulate how technical work is delivered in an engineering environment.

Each sprint includes:

* A clear technical goal
* Deliverables
* Validation steps
* Documentation
* Lessons learned
* Incremental improvement

More details are available in:

[Agile Scrum-Inspired Process](docs/agile-scrum-process.md)

## Python Test Simulator

The main simulation script is:

```text
app/fake_chip_test.py
```

The script simulates test execution for semiconductor-related components such as ASICs and FPGAs.

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

The output is saved to:

```text
reports/test_results.csv
```

## Performance Benchmarking

The simulator includes basic performance benchmarking by measuring:

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

The Jenkins pipeline automates the full workflow.

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
Application Health Checks
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
* Runs application health checks.
* Archives the CSV report, dashboard HTML, and health check report as build artifacts.

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

Database:

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

After importing the CSV report into PostgreSQL, SQL queries validate the test data.

Example metrics:

```text
Total records: 25
PASS count
FAIL count
Average duration
Slowest test
Failed test details
```

Example queries:

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

Local dashboard URL:

```text
http://192.168.159.135:8081
```

Dashboard generation script:

```text
app/generate_dashboard.py
```

The script reads metrics from PostgreSQL and generates an HTML dashboard.

The dashboard displays:

* Jenkins pipeline status
* Total test records
* PASS count
* FAIL count
* Average test duration
* Slowest test
* Failed test details
* Current architecture

The generated dashboard is published to:

```text
/var/www/semiconductor-dashboard/index.html
```

Nginx serves the dashboard on port:

```text
8081
```

## Application Health Checks

This project includes an automated health check stage that validates the main services and components used by the lab.

Health check script:

```text
app/health_check.py
```

The health check validates:

* Jenkins service status
* PostgreSQL service status
* Nginx service status
* Jenkins port `8080`
* PostgreSQL port `5432`
* Nginx dashboard port `8081`
* Dashboard HTTP response
* PostgreSQL test result records

The health check report is generated at:

```text
reports/health_check_report.txt
```

The report is archived by Jenkins as a build artifact.

More details are available in:

[Application Health Checks Documentation](docs/health-checks.md)

## Jenkins Artifacts

The Jenkins pipeline archives important output files as build artifacts.

Archived artifacts include:

```text
reports/test_results.csv
dashboard/index.html
reports/health_check_report.txt
```

These artifacts provide evidence of:

* Test results generated by the simulator
* Dashboard HTML generated from PostgreSQL metrics
* Health check validation results

## How to Run the Test Simulator Manually

From the project root directory, run:

```bash
python3 app/fake_chip_test.py
```

After execution, the script generates:

```text
reports/test_results.csv
```

To view the report:

```bash
cat reports/test_results.csv
```

## How to Run SQL Metrics Manually

To execute SQL metrics against PostgreSQL:

```bash
PGPASSWORD='<postgres-password>' psql -h localhost -U lab_user -d semiconductor_lab -f sql/metrics_queries.sql
```

This runs the SQL validation queries stored in:

```text
sql/metrics_queries.sql
```

## How to Generate the Dashboard Manually

To generate the dashboard manually from PostgreSQL metrics:

```bash
DB_PASSWORD='<postgres-password>' python3 app/generate_dashboard.py
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

## How to Run Health Checks Manually

To run the health check script manually:

```bash
DB_PASSWORD='<postgres-password>' python3 app/health_check.py
```

This generates:

```text
reports/health_check_report.txt
```

## Troubleshooting Documentation

This project includes incident documentation based on real issues encountered during the lab.

Current incident reports:

* [Incident 001: Ubuntu Server VM Network Issue - DHCP and Netplan](docs/incident-001-ubuntu-network-dhcp-netplan.md)
* [Incident 002: Jenkins Pipeline Failed Due to Missing PostgreSQL Credential](docs/incident-002-jenkins-missing-postgresql-credential.md)
* [Incident 003: Jenkins Failed to Generate Nginx Dashboard Due to Linux File Permissions](docs/incident-003-jenkins-nginx-permission-denied.md)

Each incident document includes:

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

* Supporting Linux-based tools
* Working from a Windows workstation
* Using SSH for remote access
* Managing code with Git and GitHub
* Automating technical workflows
* Running Jenkins CI/CD pipelines
* Managing credentials securely in Jenkins
* Generating and reviewing test reports
* Storing application-generated data in PostgreSQL
* Running SQL queries for validation and metrics
* Publishing dashboards with Nginx
* Validating services, ports, HTTP endpoints, and database records
* Troubleshooting Linux permissions
* Reviewing Jenkins console output
* Documenting incidents and resolutions
* Working with Scrum-inspired project structure

## Application Support Relevance

This project demonstrates a simplified version of workflows that an Application Support Engineer may support in a real engineering environment.

It includes:

* Linux server administration
* Windows-to-Linux remote access
* GitHub-based source control
* Jenkins pipeline execution
* Jenkins credential usage
* Python-based automation
* CSV report generation
* PostgreSQL data storage
* SQL metrics validation
* Nginx dashboard publishing
* Service and port health checks
* Linux file permission troubleshooting
* Technical documentation
* Incident documentation
* Incremental delivery using Scrum-inspired practices

In a real environment, similar workflows may be used to support internal engineering tools, automated test systems, build pipelines, performance reporting, operational dashboards, and troubleshooting processes.

## Future Improvements

Planned next steps:

1. Explore STDF-related concepts for semiconductor test data processing.
2. Add additional troubleshooting scenarios for service failures.
3. Improve dashboard styling and add more metrics.
4. Add historical build trend tracking.
5. Add automated alerting concepts.
6. Add dashboard uptime and response time tracking.

## Learning Goal

The main goal of this project is not to perform real semiconductor testing, but to simulate the type of technical workflow an Application Support Engineer might support in an engineering environment.

This includes automation, pipeline execution, data validation, monitoring, troubleshooting, SQL metrics, dashboard publishing, and technical documentation.
