# Semiconductor Test Support Lab

This project simulates a basic Application Support Engineering environment inspired by semiconductor test automation workflows.

The goal of this lab is to practice Linux administration, Git/GitHub, Python scripting, CI/CD concepts, performance benchmarking, test result reporting, troubleshooting, and technical documentation.

This project starts with simulated semiconductor test data and is designed to evolve into a more realistic test data pipeline using Jenkins, PostgreSQL, Nginx, and STDF-related concepts.

## Project Purpose

In engineering environments, internal tools are often used to automate testing, collect results, store metrics, and help teams identify failures quickly.

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
Future: PostgreSQL Database
   ↓
Future: Nginx Dashboard
```

## Agile Scrum-Inspired Workflow

This project is organized using Scrum-inspired practices to simulate how technical work is delivered in an engineering environment.

The lab is divided into implementation sprints, each with a clear goal, deliverables, validation steps, and documentation.

Current sprint structure:

* Sprint 1: Ubuntu Server, SSH, Git, GitHub, and Python test simulation.
* Sprint 2: Jenkins CI/CD pipeline execution.
* Sprint 3: PostgreSQL integration.
* Sprint 4: Nginx dashboard.
* Sprint 5: Monitoring and troubleshooting documentation.
* Sprint 6: STDF-related semiconductor test data concepts.

More details are available in:

[Agile Scrum-Inspired Process](docs/agile-scrum-process.md)

## Current Features

* Ubuntu Server VM configured.
* Network connectivity fixed using Netplan.
* SSH access enabled from Windows.
* Git and GitHub configured.
* Python test simulation script created.
* Simulated ASIC/FPGA test results generated.
* CSV report generated with PASS/FAIL results.
* Basic performance benchmarking included.
* Jenkins installed and configured.
* Jenkins pipeline created using a `Jenkinsfile`.
* Jenkins build executed successfully.
* CSV report archived as a Jenkins build artifact.
* Technical documentation created for troubleshooting, Jenkins, and Scrum-inspired workflow.

## Technologies Used

* Ubuntu Server
* Windows PowerShell
* SSH
* Git
* GitHub
* Python
* CSV reporting
* Jenkins
* CI/CD pipeline concepts
* Markdown technical documentation

## Technologies Planned

* PostgreSQL
* Nginx
* Application monitoring
* STDF / semiconductor test data concepts

## Project Structure

```text
semiconductor-test-support-lab/
│
├── app/
│   └── fake_chip_test.py
│
├── docs/
│   ├── agile-scrum-process.md
│   ├── incident-001-ubuntu-network-dhcp-netplan.md
│   └── jenkins-pipeline.md
│
├── reports/
│   └── test_results.csv
│
├── sql/
│
├── Jenkinsfile
└── README.md
```

## Python Test Simulator

The current Python script simulates test execution for different semiconductor-related components, including ASICs and FPGAs.

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
Average test duration: 0.742 seconds
Slowest test: Frequency Test on FPGA-2001 - 1.17 seconds
Total pipeline duration: 18.6 seconds
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
Archived Build Artifact
```

The pipeline performs the following actions:

* Verifies that Python is available.
* Runs the semiconductor test simulation script.
* Displays the generated CSV report in the Jenkins console output.
* Archives the CSV report as a Jenkins build artifact.

More details are available in:

[Jenkins Pipeline Documentation](docs/jenkins-pipeline.md)

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

## Why This Lab Matters

This lab is designed to practice skills commonly used in Application Support Engineering environments:

* Supporting Linux-based tools.
* Working from a Windows workstation.
* Using SSH for remote access.
* Managing code with Git and GitHub.
* Automating technical workflows.
* Generating and reviewing test reports.
* Understanding performance metrics.
* Preparing for CI/CD pipeline support.
* Documenting troubleshooting scenarios.
* Working with Scrum-inspired project structure.

## Future Improvements

Planned next steps:

1. Store test results in PostgreSQL.
2. Build a simple Nginx dashboard to display test metrics.
3. Add monitoring documentation for common support scenarios.
4. Explore STDF-related concepts for semiconductor test data processing.

## Learning Goal

The main goal of this project is not to perform real semiconductor testing, but to simulate the type of technical workflow an Application Support Engineer might support in an engineering environment.

This includes automation, pipeline execution, data validation, monitoring, troubleshooting, and technical documentation.
