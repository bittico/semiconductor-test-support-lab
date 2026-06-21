# Incident 003: Jenkins Failed to Generate Nginx Dashboard Due to Linux File Permissions

## Summary

During the Nginx dashboard automation phase, the Jenkins pipeline was updated to generate an HTML dashboard from PostgreSQL metrics and publish it to the Nginx web directory.

The pipeline successfully executed the Python simulator, generated the CSV report, imported the results into PostgreSQL, and ran SQL metrics validation. However, it failed when trying to write the generated dashboard file to the Nginx directory.

## Environment

* CI/CD Tool: Jenkins
* Web Server: Nginx
* Operating System: Ubuntu Server
* Database: PostgreSQL
* Source Control: GitHub
* Dashboard Path: `/var/www/semiconductor-dashboard/index.html`
* Jenkins Workspace: `/var/lib/jenkins/workspace/semiconductor-test-support-lab-pipeline`

## Issue

The Jenkins pipeline failed during the dashboard generation stage.

Failed stage:

```text
Generate Nginx Dashboard
```

The console output showed the following error:

```text
PermissionError: [Errno 13] Permission denied: '/var/www/semiconductor-dashboard/index.html'
```

Final result:

```text
Finished: FAILURE
```

## What Worked Correctly

Before the failure, the pipeline successfully completed the following stages:

* Repository checkout from GitHub.
* Python version validation.
* Semiconductor test simulation execution.
* CSV report generation.
* PostgreSQL import.
* SQL metrics validation.

The PostgreSQL import completed successfully:

```text
DELETE 25
COPY 25
```

SQL metrics validation also worked correctly:

```text
total_records: 25
PASS/FAIL summary generated
average_duration_seconds generated
failed test details generated
```

This confirmed that the issue was not related to GitHub, Python, PostgreSQL, SQL queries, or Jenkins credentials.

## Investigation

The failure occurred when the Python dashboard generation script attempted to write the generated HTML file to:

```text
/var/www/semiconductor-dashboard/index.html
```

The Jenkins pipeline runs under the Linux user:

```text
jenkins
```

The Nginx dashboard directory had been created manually, and the file permissions did not allow the `jenkins` user to overwrite the `index.html` file.

## Root Cause

The root cause was insufficient Linux file permissions on the Nginx dashboard directory.

The `jenkins` user did not have write permission to:

```text
/var/www/semiconductor-dashboard/index.html
```

As a result, Jenkins could generate the dashboard content but could not publish it to the Nginx web directory.

## Resolution

The ownership and permissions of the dashboard directory were updated so that both the `turista` user and the `jenkins` group could write to the directory.

Commands used:

```bash
sudo chown -R turista:jenkins /var/www/semiconductor-dashboard
sudo chmod -R 775 /var/www/semiconductor-dashboard
sudo chmod g+s /var/www/semiconductor-dashboard
```

## Command Explanation

The following command changed the owner and group:

```bash
sudo chown -R turista:jenkins /var/www/semiconductor-dashboard
```

Meaning:

* Owner: `turista`
* Group: `jenkins`
* Applied recursively to all files inside the dashboard directory

The following command granted write permissions to the owner and group:

```bash
sudo chmod -R 775 /var/www/semiconductor-dashboard
```

Meaning:

* Owner can read, write, and execute.
* Group can read, write, and execute.
* Others can read and execute.

The following command enabled group inheritance:

```bash
sudo chmod g+s /var/www/semiconductor-dashboard
```

Meaning:

* New files created inside the directory inherit the `jenkins` group.
* This helps prevent future permission issues.

## Validation

After updating the permissions, the Jenkins pipeline was executed again.

The dashboard generation stage completed successfully.

The dashboard was available through Nginx at:

```text
http://192.168.159.135:8081
```

The dashboard displayed updated PostgreSQL metrics, including:

* Total records
* PASS count
* FAIL count
* Average duration
* Slowest test
* Failed test details

Final result:

```text
Finished: SUCCESS
```

## Lessons Learned

* Jenkins runs pipeline commands as the Linux `jenkins` user.
* A script may work manually as one user but fail in Jenkins due to different permissions.
* Web directories under `/var/www` require careful ownership and permission management.
* Linux file permissions are critical when CI/CD tools publish files to web server directories.
* The first meaningful error in the Jenkins console output usually identifies the real root cause.
* Validating permissions with the same user that runs the pipeline is an important troubleshooting step.

## Application Support Relevance

This incident demonstrates a realistic Application Support Engineering troubleshooting scenario involving:

* Jenkins pipeline execution.
* Linux file permissions.
* Nginx web directory publishing.
* Python automation.
* PostgreSQL-backed dashboard generation.
* Console log analysis.
* Root cause analysis.
* Validation after remediation.

In a real environment, similar issues may happen when CI/CD pipelines publish reports, dashboards, build artifacts, or generated files to shared application directories or web servers.
