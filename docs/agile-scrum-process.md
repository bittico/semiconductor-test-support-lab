# Agile Scrum-Inspired Process

## Overview

This project is organized using Scrum-inspired practices to simulate how technical work is delivered in an engineering environment.

Although this is an individual learning project, it follows Agile Scrum concepts such as backlog management, sprint planning, sprint goals, definition of done, validation, documentation, and retrospective notes.

The goal is to build the lab incrementally through small, manageable phases, each one delivering a working technical improvement.

## Scrum-Inspired Approach

The project is divided into sprints. Each sprint has a clear technical goal, deliverables, validation steps, and documentation.

| Sprint   | Goal                                                                    | Status    |
| -------- | ----------------------------------------------------------------------- | --------- |
| Sprint 1 | Set up Ubuntu Server, SSH, Git, GitHub, and Python test simulation      | Completed |
| Sprint 2 | Install Jenkins and create a CI/CD pipeline to run the Python simulator | Completed |
| Sprint 3 | Add PostgreSQL to store test results and query metrics                  | Completed |
| Sprint 4 | Add Nginx dashboard generated from PostgreSQL metrics                   | Completed |
| Sprint 5 | Add monitoring checks and additional troubleshooting documentation      | Planned   |
| Sprint 6 | Add STDF-related semiconductor test data concepts                       | Planned   |

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
* Document troubleshooting incidents.

### Planned Backlog Items

* Add service health checks for Jenkins, PostgreSQL, and Nginx.
* Add monitoring scripts.
* Add more troubleshooting scenarios.
* Improve dashboard styling and metrics.
* Explore STDF-related semiconductor test data concepts.

## Sprint Details

## Sprint 1: Linux, SSH, GitHub, and Python Simulator

### Sprint Goal

Build the base Linux environment and create a Python script that simulates semiconductor test execution.

### Deliverables

* Ubuntu Server VM configured.
* SSH access from Windows.
* Git and GitHub repository configured.
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
* Dashboard available from Windows browser.
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

## Definition of Done

A task is considered done when:

* The technical implementation works successfully.
* The command or configuration has been validated.
* The change is committed to Git.
* The change is pushed to GitHub.
* The README or technical documentation is updated if needed.
* Any relevant issue or troubleshooting step is documented.
* The Jenkins pipeline is updated if automation is required.
* The result can be validated from the expected user interface, command, log, or service endpoint.

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
* Documentation is important because it shows not only what was built, but also how issues were investigated and resolved.

## Application Support Relevance

This Scrum-inspired approach demonstrates skills relevant to an Application Support Engineering role:

* Working in structured phases.
* Managing a technical backlog.
* Supporting tools used by engineering teams.
* Troubleshooting Linux, Windows, networking, Jenkins, PostgreSQL, and Nginx issues.
* Documenting incidents and resolutions.
* Delivering incremental improvements.
* Reviewing logs and validating results.
* Automating manual processes.
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
Archived Artifacts
```

Current status:

```text
Sprint 1: Completed
Sprint 2: Completed
Sprint 3: Completed
Sprint 4: Completed
Sprint 5: Planned
Sprint 6: Planned
```
