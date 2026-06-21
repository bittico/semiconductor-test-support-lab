# Incident 002: Jenkins Pipeline Failed Due to Missing PostgreSQL Credential

## Summary

During the Jenkins pipeline improvement phase, the project was updated to use Jenkins Credentials instead of storing the PostgreSQL password directly in the `Jenkinsfile`.

After updating the pipeline, the Jenkins build failed because the credential ID referenced in the `Jenkinsfile` did not exist yet in Jenkins.

## Environment

* CI/CD Tool: Jenkins
* Source Control: GitHub
* Operating System: Ubuntu Server
* Database: PostgreSQL
* Pipeline File: `Jenkinsfile`
* Credential ID: `postgres-lab-password`

## Issue

The Jenkins pipeline failed shortly after checking out the repository from GitHub.

The console output showed:

```text
ERROR: postgres-lab-password
Finished: FAILURE
```

The pipeline did not continue to the normal execution stages such as:

* Verify Python
* Run Semiconductor Test Simulation
* Import CSV into PostgreSQL
* Run SQL Metrics Validation

## Investigation

The Jenkins console output confirmed that the repository checkout was successful:

```text
Obtained Jenkinsfile from git https://github.com/bittico/semiconductor-test-support-lab.git
```

It also confirmed that Jenkins was using the latest commit:

```text
Commit message: "Use Jenkins credentials for PostgreSQL password"
```

This indicated that GitHub and the `Jenkinsfile` checkout were working correctly.

The failure occurred because the `Jenkinsfile` referenced the following credential:

```groovy
DB_PASSWORD = credentials('postgres-lab-password')
```

However, Jenkins did not have a credential with that exact ID.

## Root Cause

The PostgreSQL password was moved from plain text in the `Jenkinsfile` to Jenkins Credentials, but the credential was not yet created in Jenkins.

Jenkins could not find the credential ID:

```text
postgres-lab-password
```

## Resolution

A new Jenkins credential was created under:

```text
Manage Jenkins
Credentials
System
Global credentials
Add Credentials
```

The credential was configured as:

```text
Kind: Secret text
Secret: lab_password
ID: postgres-lab-password
Description: PostgreSQL lab password
```

After creating the credential, the pipeline was executed again.

## Validation

The next Jenkins build completed successfully.

The console output showed that Jenkins masked the PostgreSQL password:

```text
Masking supported pattern matches of $DB_PASSWORD
PGPASSWORD=****
```

The PostgreSQL import also completed successfully:

```text
DELETE 25
COPY 25
```

SQL metrics validation executed correctly:

```text
total_records: 25
FAIL: 3
PASS: 22
average_duration_seconds: 0.659
```

Final result:

```text
Finished: SUCCESS
```

## Lessons Learned

* Credential IDs in Jenkins must match exactly what is referenced in the `Jenkinsfile`.
* Secrets should not be stored directly in source control.
* Jenkins Credentials provide a safer way to manage passwords and tokens.
* Console output should be reviewed carefully to identify the true root cause.
* A secondary error may appear after the main failure, but the first meaningful error usually points to the real issue.

## Application Support Relevance

This incident demonstrates a realistic Application Support and CI/CD troubleshooting scenario.

The troubleshooting process included:

* Reviewing Jenkins console output.
* Validating GitHub checkout.
* Identifying the failing pipeline stage.
* Understanding Jenkins Credentials.
* Correcting the missing credential configuration.
* Re-running the pipeline.
* Validating successful database import and SQL metrics execution.

This type of issue is common in real CI/CD environments where pipelines depend on external systems, credentials, databases, and automation tools.
