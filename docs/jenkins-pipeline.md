# Jenkins Pipeline Documentation

## Overview

This project uses Jenkins to automate the execution of a Python-based semiconductor test simulation.

The pipeline reads the source code from the GitHub repository, executes the Python script, generates a CSV report, displays the report in the build logs, and archives the generated report as a Jenkins build artifact.

This simulates a basic CI/CD workflow that an Application Support Engineer may support in an engineering environment.

## Pipeline Flow

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

## Jenkinsfile Purpose

The `Jenkinsfile` defines the steps Jenkins must execute.

Instead of running the Python script manually from the Linux terminal, Jenkins reads the pipeline instructions and executes the process automatically.

This makes the workflow repeatable, visible, and easier to troubleshoot.

## Pipeline Stages

### 1. Verify Python

This stage validates that Python is available on the Jenkins server.

Command executed:

```bash
python3 --version
```

Purpose:

* Confirm that Python is installed.
* Validate that the environment is ready before running the application script.
* Fail early if the required runtime is missing.

### 2. Run Semiconductor Test Simulation

This stage runs the Python script that simulates semiconductor test execution.

Command executed:

```bash
python3 app/fake_chip_test.py
```

Purpose:

* Execute simulated ASIC and FPGA test cases.
* Generate PASS/FAIL test results.
* Measure execution time.
* Create the CSV report.

### 3. Show Generated Report

This stage displays the generated CSV report in the Jenkins console output.

Command executed:

```bash
cat reports/test_results.csv
```

Purpose:

* Validate that the report was generated.
* Make the output visible in the build logs.
* Help with troubleshooting if the report content is incorrect.

## Build Artifact

The pipeline archives the generated CSV file:

```text
reports/test_results.csv
```

This means Jenkins stores the report inside the build result.

Artifacts are useful because they provide evidence of what was generated during a specific pipeline execution.

## Successful Build Result

A successful Jenkins build confirms that:

* Jenkins can access the project files.
* The `Jenkinsfile` syntax is valid.
* Python is available on the server.
* The simulation script runs correctly.
* The CSV report is generated.
* The report can be archived as a build artifact.

## Application Support Relevance

This Jenkins pipeline demonstrates skills relevant to an Application Support Engineering role:

* CI/CD pipeline execution.
* Linux-based automation.
* GitHub repository integration.
* Build log analysis.
* Artifact validation.
* Basic troubleshooting of automated workflows.
* Supporting tools used by engineering teams.

In a real engineering environment, a similar pipeline could be used to run builds, execute automated tests, generate reports, validate engineering tools, or support internal development workflows.

## Current Status

The Jenkins pipeline was successfully created and executed.

Current result:

```text
Build Status: SUCCESS
```
