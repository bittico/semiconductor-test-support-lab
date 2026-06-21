# Application Health Checks Documentation

## Overview

This project includes an application health check script used to validate the main services and components involved in the lab environment.

The health check is executed as part of the Jenkins pipeline after the Python simulation, PostgreSQL import, SQL metrics validation, and Nginx dashboard generation are completed.

This simulates a common Application Support Engineering task: validating that all required services, ports, endpoints, and application data are available after an automated workflow runs.

## Health Check Script

The health check script is located at:

```text
app/health_check.py
```

The script generates a text report at:

```text
reports/health_check_report.txt
```

The report is archived by Jenkins as a build artifact.

## Components Validated

The health check validates the following components:

* Jenkins service
* PostgreSQL service
* Nginx service
* Jenkins port `8080`
* PostgreSQL port `5432`
* Nginx dashboard port `8081`
* Nginx dashboard HTTP response
* PostgreSQL test result records

## Validation Flow

The health check runs after the main pipeline stages:

```text
GitHub Repository
   ↓
Jenkins Pipeline
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
```

## Checks Performed

### 1. Jenkins Service Status

The script validates that the Jenkins service is active.

Example result:

```text
[PASS] jenkins: active
```

### 2. PostgreSQL Service Status

The script validates that PostgreSQL is active.

Example result:

```text
[PASS] postgresql: active
```

### 3. Nginx Service Status

The script validates that Nginx is active.

Example result:

```text
[PASS] nginx: active
```

### 4. Jenkins Port Check

The script validates that Jenkins is reachable on port `8080`.

Example result:

```text
[PASS] Jenkins port 8080: reachable
```

### 5. PostgreSQL Port Check

The script validates that PostgreSQL is reachable on port `5432`.

Example result:

```text
[PASS] PostgreSQL port 5432: reachable
```

### 6. Nginx Dashboard Port Check

The script validates that the Nginx dashboard is reachable on port `8081`.

Example result:

```text
[PASS] Nginx Dashboard port 8081: reachable
```

### 7. Dashboard HTTP Check

The script validates that the dashboard returns an HTTP `200` response.

Example result:

```text
[PASS] Nginx Dashboard HTTP: HTTP 200
```

### 8. PostgreSQL Data Check

The script validates that the `test_results` table contains the expected number of records.

Example result:

```text
[PASS] PostgreSQL data check: 25 records found
```

## Jenkins Pipeline Integration

The Jenkins pipeline includes a stage called:

```text
Run Application Health Checks
```

This stage executes:

```bash
python3 app/health_check.py
```

Because the pipeline already injects the PostgreSQL password using Jenkins Credentials, the health check script can connect to the database without storing the password directly in source control.

## Build Artifact

The health check report is archived by Jenkins as a build artifact.

Archived file:

```text
reports/health_check_report.txt
```

This provides evidence that the environment was validated during the pipeline execution.

## Successful Result

A successful health check confirms that:

* Jenkins is running.
* PostgreSQL is running.
* Nginx is running.
* Required ports are reachable.
* The dashboard responds over HTTP.
* PostgreSQL contains the expected test data.
* The application support workflow is healthy after pipeline execution.

Example final result:

```text
Total checks: 8
Passed: 8
Failed: 0
Finished: SUCCESS
```

## Application Support Relevance

This health check stage demonstrates skills relevant to an Application Support Engineering role:

* Service validation
* Port connectivity testing
* HTTP endpoint validation
* Database data validation
* Jenkins pipeline validation
* Artifact review
* Operational readiness checks
* Troubleshooting preparation

In a real environment, similar checks may be used after deployments, scheduled jobs, test pipeline executions, application restarts, or incident recovery actions.
