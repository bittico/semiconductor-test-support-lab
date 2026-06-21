# Jenkins PostgreSQL Automation Documentation

## Overview

This document describes the Jenkins pipeline automation used in this project to execute a Python semiconductor test simulation, generate a CSV report, import the results into PostgreSQL, run SQL metrics validation, and archive the generated report as a Jenkins build artifact.

This expands the original pipeline from a simple Python execution workflow into a more complete Application Support Engineering workflow that includes application execution, data persistence, database validation, and build artifact management.

## Automated Pipeline Flow

The current automated workflow is:

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
Archived Build Artifact
```

## Pipeline Source

Jenkins obtains the pipeline definition directly from the GitHub repository.

Example from the Jenkins console output:

```text
Obtained Jenkinsfile from git https://github.com/bittico/semiconductor-test-support-lab.git
```

This confirms that Jenkins is not running manually pasted commands. Instead, it reads the `Jenkinsfile` stored in source control.

## Pipeline Stages

### 1. Verify Python

This stage validates that Python is available on the Jenkins server.

Command executed:

```bash
python3 --version
```

Example result:

```text
Python 3.14.4
```

Purpose:

* Confirm that the required runtime exists.
* Validate the execution environment before running the simulator.
* Fail early if Python is missing.

### 2. Run Semiconductor Test Simulation

This stage runs the Python script that simulates semiconductor test execution.

Command executed:

```bash
python3 app/fake_chip_test.py
```

Example output:

```text
Total tests executed: 25
Passed: 18
Failed: 7
Pass rate: 72.0%
Average test duration: 0.721 seconds
Report generated at: reports/test_results.csv
```

Purpose:

* Execute simulated ASIC and FPGA test cases.
* Generate PASS/FAIL test results.
* Measure test execution time.
* Create a CSV report.

### 3. Show Generated Report

This stage displays the generated CSV report in the Jenkins console output.

Command executed:

```bash
cat reports/test_results.csv
```

Purpose:

* Confirm that the report was generated.
* Make the report visible in the Jenkins logs.
* Help troubleshoot incorrect or missing output.

### 4. Import CSV into PostgreSQL

This stage imports the generated CSV report into the PostgreSQL database.

The pipeline first deletes the previous test records and then imports the new CSV results.

Example Jenkins console output:

```text
DELETE 25
COPY 25
```

Meaning:

* `DELETE 25` means Jenkins removed the previous 25 records from the `test_results` table.
* `COPY 25` means Jenkins imported 25 new records from the CSV report into PostgreSQL.

Purpose:

* Keep the database synchronized with the latest pipeline execution.
* Avoid duplicate records between builds.
* Store application-generated data in a relational database.

### 5. Run SQL Metrics Validation

This stage executes SQL queries from:

```text
sql/metrics_queries.sql
```

The validation queries confirm that the imported data is available and can be analyzed.

Example validation results:

```text
total_records: 25
FAIL: 7
PASS: 18
average_duration_seconds: 0.721
```

The queries also identify:

* Total number of records.
* PASS/FAIL distribution.
* Average test duration.
* Slowest test execution.
* Failed test details.

Purpose:

* Validate that the database import worked.
* Confirm that metrics can be extracted using SQL.
* Simulate operational reporting and data validation tasks.

### 6. Archive Build Artifact

The pipeline archives the generated CSV report as a Jenkins build artifact.

Archived file:

```text
reports/test_results.csv
```

Purpose:

* Preserve the output of each build.
* Provide evidence of what was generated during the pipeline run.
* Allow comparison between different executions.

## Successful Build Result

The Jenkins build completed successfully.

Build result:

```text
Finished: SUCCESS
```

This confirms that:

* Jenkins pulled the project from GitHub.
* Jenkins read the `Jenkinsfile`.
* Python was available.
* The simulation script executed correctly.
* The CSV report was generated.
* PostgreSQL import completed successfully.
* SQL metrics validation executed successfully.
* The CSV report was archived as a build artifact.

## Application Support Relevance

This automation demonstrates skills relevant to an Application Support Engineering role:

* CI/CD pipeline execution.
* Jenkins pipeline troubleshooting.
* Linux-based automation.
* GitHub source control integration.
* Python script execution.
* CSV report generation.
* PostgreSQL data import.
* SQL metrics validation.
* Build log review.
* Artifact validation.
* Technical documentation.

In a real engineering environment, similar workflows may be used to support internal tools, automated tests, build systems, test result pipelines, performance reporting, or operational dashboards.

## Current Status

Current automation status:

```text
GitHub → Jenkins → Python Simulator → CSV Report → PostgreSQL Import → SQL Metrics Validation → Archived Artifact
```

Status:

```text
Completed successfully
```
