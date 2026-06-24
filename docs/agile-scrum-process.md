# Agile Scrum-Inspired Process

## Overview

This project is organized using Scrum-inspired practices to simulate how technical work is delivered in an engineering support environment.

Although this is an individual learning project, it follows Agile Scrum concepts such as backlog management, sprint planning, sprint goals, definition of done, validation, documentation, and retrospective notes.

The goal is to build the lab incrementally through small, manageable phases. Each sprint delivers a working technical improvement and adds documentation that explains the implementation, validation, and lessons learned.

## Scrum-Inspired Approach

The project is divided into sprints. Each sprint has a clear technical goal, deliverables, validation steps, and documentation.

| Sprint   | Goal                                                                    | Status    |
| -------- | ----------------------------------------------------------------------- | --------- |
| Sprint 1 | Set up Ubuntu Server, SSH, Git, GitHub, and Python test simulation      | Completed |
| Sprint 2 | Install Jenkins and create a CI/CD pipeline to run the Python simulator | Completed |
| Sprint 3 | Add PostgreSQL to store test results and query metrics                  | Completed |
| Sprint 4 | Add Nginx dashboard generated from PostgreSQL metrics                   | Completed |
| Sprint 5 | Add application health checks and monitoring validation                 | Completed |
| Sprint 6 | Add STDF-inspired semiconductor test data concepts                      | Completed |

## Product Backlog

The product backlog contains the main technical tasks required to complete the lab.

### Completed Backlog Items

* Configure Ubuntu Server networking.
* Enable SSH access from Windows.
* Create GitHub repository.
* Build Python semiconductor test simulator.
* Generate CSV test reports.
* Install Jenkins.
* Create Jenkins pipeline.
* Archive generated reports as build artifacts.
* Install PostgreSQL.
* Create PostgreSQL database.
* Create `test_results` table.
* Import CSV report into PostgreSQL.
* Create SQL metrics queries.
* Automate PostgreSQL import from Jenkins.
* Configure Jenkins Credentials for PostgreSQL password.
* Install Nginx.
* Configure Nginx dashboard on port `8081`.
* Generate dashboard HTML from PostgreSQL metrics.
* Automate dashboard generation from Jenkins.
* Validate dashboard file from Jenkins.
* Create application health check script.
* Validate Jenkins, PostgreSQL, Nginx, ports, HTTP response, and database records.
* Archive health check reports in Jenkins.
* Create STDF-inspired semiconductor test data generator.
* Create STDF-inspired yield processor.
* Generate STDF-inspired yield summary reports.
* Generate STDF-inspired yield breakdown reports.
* Validate STDF-inspired reports from Jenkins.
* Archive STDF-inspired reports in Jenkins.
* Document STDF-inspired semiconductor test data concepts.
* Document troubleshooting incidents.

### Planned Backlog Items

* Create a real Jira Service Management project for support-style ticket tracking.
* Add a PowerShell validation script from Windows.
* Add a FlexLM-inspired license availability check.
* Add Ansible-based server automation.
* Add Artifactory-style artifact and release management concepts.
* Add cloud-ready architecture documentation.
* Improve dashboard styling and metrics.
* Add historical build trend tracking.
* Add automated alerting concepts.

## Sprint Details

## Sprint 1: Linux, SSH, GitHub, and Python Simulator

### Sprint Goal

Build the base Linux environment and create a Python script that simulates semiconductor test execution.

### Deliverables

* Ubuntu Server VM configured.
* SSH access from Windows.
* Git installed.
* GitHub repository created.
* Python semiconductor test simulator created.
* CSV report generated.
* Initial troubleshooting documentation created.

### Validation

* Ubuntu received an IPv4 address.
* SSH connection worked from Windows.
* Python script executed successfully.
* CSV file was generated.
* Changes were committed and pushed to GitHub.

### Status

Completed.

## Sprint 2: Jenkins CI/CD Pipeline

### Sprint Goal

Automate the execution of the Python simulator using Jenkins.

### Deliverables

* Jenkins installed on Ubuntu Server.
* Jenkins pipeline job created.
* `Jenkinsfile` added to GitHub.
* Pipeline connected to the GitHub repository.
* Pipeline executed Python script.
* CSV report archived as Jenkins build artifact.
* Jenkins pipeline documentation created.

### Validation

* Jenkins accessed the GitHub repository.
* Jenkins read the `Jenkinsfile`.
* Pipeline executed successfully.
* CSV report was archived as an artifact.
* Build completed with `SUCCESS`.

### Status

Completed.

## Sprint 3: PostgreSQL Integration and SQL Metrics

### Sprint Goal

Store test results in PostgreSQL and validate them using SQL queries.

### Deliverables

* PostgreSQL installed.
* Database `semiconductor_lab` created.
* User `lab_user` created.
* Table `test_results` created.
* CSV report imported into PostgreSQL.
* SQL metrics queries created.
* Jenkins pipeline updated to automate PostgreSQL import.
* Jenkins Credentials configured for PostgreSQL password.
* PostgreSQL integration documentation created.
* Jenkins PostgreSQL automation documentation created.

### Validation

* CSV import returned `COPY 25`.
* SQL query confirmed 25 records.
* PASS/FAIL count query returned expected results.
* Average duration query returned a valid metric.
* Jenkins masked the database password using `PGPASSWORD=****`.
* Jenkins build completed with `SUCCESS`.

### Status

Completed.

## Sprint 4: Nginx Dashboard

### Sprint Goal

Publish a web dashboard using Nginx and generate its content from PostgreSQL metrics.

### Deliverables

* Nginx installed.
* Nginx configured to serve the dashboard on port `8081`.
* Dashboard HTML created.
* Python dashboard generator created.
* Dashboard generated from PostgreSQL metrics.
* Jenkins pipeline updated to generate the dashboard automatically.
* Jenkins pipeline validates the dashboard file.
* Dashboard available from a Windows browser.
* Linux permission issue documented as an incident.

### Validation

* Nginx service was active.
* Dashboard opened successfully at `http://192.168.159.135:8081`.
* Dashboard displayed PostgreSQL metrics.
* Jenkins generated the dashboard automatically.
* Jenkins validated the dashboard file.
* Jenkins build completed with `SUCCESS`.

### Status

Completed.

## Sprint 5: Monitoring and Health Checks

### Sprint Goal

Add automated health checks to validate the main services and components used by the application support lab.

### Deliverables

* Health check script created.
* Jenkins service validation added.
* PostgreSQL service validation added.
* Nginx service validation added.
* Port checks added for Jenkins, PostgreSQL, and Nginx dashboard.
* Dashboard HTTP validation added.
* PostgreSQL data validation added.
* Jenkins pipeline updated to run health checks automatically.
* Health check report archived as a Jenkins build artifact.
* Health check documentation created.

### Validation

* Jenkins pipeline executed the health check stage successfully.
* Health check validated 8 components.
* All checks passed.
* Health check report was generated.
* Jenkins archived the health check report as a build artifact.
* Pipeline completed with `SUCCESS`.

### Status

Completed.

## Sprint 6: STDF-Inspired Semiconductor Test Data

### Sprint Goal

Add an STDF-inspired semiconductor test data layer to better align the lab with semiconductor test automation workflows.

The goal was not to parse real binary STDF files, but to model common semiconductor test data concepts such as lots, wafers, test sites, testers, ASIC/FPGA device types, test numbers, measured values, limits, pass/fail results, fail reasons, and yield calculations.

### Deliverables

* STDF-inspired data generator created.
* STDF-inspired data processor created.
* Structured semiconductor test dataset generated.
* Yield summary report generated.
* Yield breakdown report generated.
* Human-readable STDF-inspired yield report generated.
* Jenkins pipeline updated with STDF-inspired stages.
* Jenkins validates STDF-inspired report files.
* Jenkins archives STDF-inspired artifacts.
* STDF concepts documentation created.
* README updated after Sprint 6 completion.

### Files Created

```text
app/generate_stdf_inspired_data.py
app/process_stdf_inspired_data.py
data/stdf_inspired_test_records.csv
reports/stdf_yield_summary.csv
reports/stdf_yield_breakdown.csv
reports/stdf_yield_report.txt
docs/stdf-concepts.md
```

### Jenkins Stages Added

```text
Generate STDF-Inspired Data
Process STDF-Inspired Data
Validate STDF Reports
```

### Validation

* Jenkins generated 360 STDF-inspired test records.
* Jenkins processed the generated dataset successfully.
* Jenkins calculated overall yield.
* Jenkins generated breakdowns by lot, wafer, site, tester, device type, test name, and fail reason.
* Jenkins validated that all expected STDF-inspired files existed.
* Jenkins validated expected report content.
* Jenkins archived the STDF-inspired data and reports as build artifacts.
* Jenkins build completed with `SUCCESS`.

### Example Result

```text
Total records: 360
Passed: 322
Failed: 38
Yield: 89.44%
```

### Application Support Relevance

This sprint demonstrates how an Application Support Engineer may support internal tools and pipelines that process engineering data.

It connects infrastructure support with semiconductor-related data concepts, including:

* ATE-inspired test records.
* ASIC and FPGA device categories.
* Lot-level analysis.
* Wafer-level analysis.
* Site-level analysis.
* Tester-level analysis.
* Yield calculation.
* Jenkins artifact validation.
* Technical documentation.

### Status

Completed.

## User Stories

### User Story 1

As an Application Support Engineer,
I want to access the Linux server remotely using SSH,
so that I can manage and troubleshoot application services from a Windows workstation.

### User Story 2

As an engineering user,
I want to run a semiconductor test simulation,
so that I can generate test results for ASIC and FPGA devices.

### User Story 3

As an Application Support Engineer,
I want Jenkins to execute the test simulation automatically,
so that the process is repeatable and does not depend on manual execution.

### User Story 4

As an Application Support Engineer,
I want generated reports to be archived in Jenkins,
so that each pipeline execution keeps evidence of its output.

### User Story 5

As an engineering team member,
I want test results to be stored in PostgreSQL,
so that I can analyze pass rates, failed tests, and execution times.

### User Story 6

As an Application Support Engineer,
I want Jenkins to import test results into PostgreSQL automatically,
so that manual database import is not required after each build.

### User Story 7

As an Application Support Engineer,
I want Jenkins to use credentials securely,
so that database passwords are not stored directly in source control.

### User Story 8

As an engineering team member,
I want a web dashboard displaying the latest test metrics,
so that results can be reviewed quickly from a browser.

### User Story 9

As an Application Support Engineer,
I want the dashboard to be generated from PostgreSQL data,
so that the web view reflects the latest pipeline execution.

### User Story 10

As an Application Support Engineer,
I want automated health checks,
so that I can validate service status, port availability, HTTP response, and database records after pipeline execution.

### User Story 11

As an Application Support Engineer,
I want to process STDF-inspired semiconductor test records,
so that I can calculate yield metrics and identify patterns by lot, wafer, site, tester, device type, and test name.

### User Story 12

As an engineering support user,
I want STDF-inspired reports to be archived in Jenkins,
so that each build keeps evidence of semiconductor-style data processing results.

## Definition of Done

A task is considered done when:

* The technical implementation works successfully.
* The command, script, service, or configuration has been validated.
* The change is committed to Git.
* The change is pushed to GitHub.
* The README or technical documentation is updated if needed.
* Any relevant issue or troubleshooting step is documented.
* Jenkins is updated if automation is required.
* Jenkins build completes successfully when pipeline changes are involved.
* Generated artifacts are validated when output files are expected.
* The result can be verified from the expected user interface, command, log, report, artifact, or service endpoint.

## Retrospective Notes

Lessons learned so far:

* Linux networking should be validated from both the Ubuntu VM and the Windows host.
* SSH troubleshooting should include service status, firewall status, IP address, routing, and host connectivity.
* VMware NAT issues can affect Windows-to-Linux connectivity even when the Linux VM is working correctly.
* Jenkins pipelines should produce visible logs and archived artifacts.
* PostgreSQL imports should be validated with SQL queries.
* Jenkins Credentials should be used instead of storing passwords directly in the `Jenkinsfile`.
* Credential IDs in Jenkins must match exactly what is referenced in the pipeline.
* Scripts may work manually but fail in Jenkins if the `jenkins` Linux user lacks permissions.
* Nginx dashboard publishing requires correct Linux file permissions.
* Health checks help validate that services are not only installed, but actually running and reachable.
* Application Support workflows should validate services, ports, HTTP endpoints, and database records.
* Jenkins artifacts are useful for preserving evidence of operational validation.
* STDF-inspired data helps connect infrastructure automation with semiconductor test concepts.
* Yield analysis can help identify patterns by lot, wafer, site, tester, device type, and test name.
* Documentation is important because it shows not only what was built, but also how issues were investigated and resolved.

## Application Support Relevance

This Scrum-inspired approach demonstrates skills relevant to an Application Support Engineering role:

* Working in structured phases.
* Managing a technical backlog.
* Supporting tools used by engineering teams.
* Troubleshooting Linux, Windows, networking, Jenkins, PostgreSQL, and Nginx issues.
* Supporting CI/CD pipelines.
* Managing credentials securely.
* Reviewing logs and validating results.
* Automating manual processes.
* Validating services and application endpoints.
* Generating operational reports.
* Processing structured engineering data.
* Reviewing yield metrics.
* Documenting incidents and resolutions.
* Delivering incremental improvements.
* Preparing for collaboration with hardware and software development teams.

## Current Project Status

Current completed workflow:

```text
GitHub
   ↓
Jenkins
   ↓
Python Simulator
   ↓
CSV Report
   ↓
PostgreSQL Import
   ↓
SQL Metrics Validation
   ↓
Python Dashboard Generator
   ↓
Nginx Dashboard
   ↓
STDF-Inspired Data Generation
   ↓
STDF-Inspired Yield Processing
   ↓
STDF Report Validation
   ↓
Application Health Checks
   ↓
Archived Artifacts
```

Current sprint status:

```text
Sprint 1: Completed
Sprint 2: Completed
Sprint 3: Completed
Sprint 4: Completed
Sprint 5: Completed
Sprint 6: Completed
```

## Next Possible Improvements

Potential next improvements include:

* Jira Service Management project for real support ticket tracking.
* PowerShell validation script from Windows.
* FlexLM-inspired license availability checks.
* Ansible-based server automation.
* Artifactory-style artifact and release management concepts.
* Cloud-ready architecture documentation.
* Additional incident scenarios.
* Dashboard enhancements.
* Historical metrics and trend tracking.
