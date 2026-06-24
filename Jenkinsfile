pipeline {
    agent any

    environment {
        DB_HOST = 'localhost'
        DB_NAME = 'semiconductor_lab'
        DB_USER = 'lab_user'
        DB_PASSWORD = credentials('postgres-lab-password')
    }

    stages {
        stage('Verify Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Semiconductor Test Simulation') {
            steps {
                sh 'python3 app/fake_chip_test.py'
            }
        }

        stage('Show Generated Report') {
            steps {
                sh 'cat reports/test_results.csv'
            }
        }

        stage('Import CSV into PostgreSQL') {
            steps {
                sh '''
                    PGPASSWORD="$DB_PASSWORD" psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" <<'SQL'
DELETE FROM test_results;
\\copy test_results(timestamp, device_id, test_name, status, duration_seconds) FROM 'reports/test_results.csv' WITH CSV HEADER;
SQL
                '''
            }
        }

        stage('Run SQL Metrics Validation') {
            steps {
                sh '''
                    PGPASSWORD="$DB_PASSWORD" psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -f sql/metrics_queries.sql
                '''
            }
        }

        stage('Generate Nginx Dashboard') {
            steps {
                sh 'python3 app/generate_dashboard.py'
            }
        }

        stage('Validate Dashboard File') {
            steps {
                sh '''
                    test -f /var/www/semiconductor-dashboard/index.html
                    grep -q "Semiconductor Test Support Dashboard" /var/www/semiconductor-dashboard/index.html
                '''
            }
        }

        stage('Generate STDF-Inspired Data') {
            steps {
                sh 'python3 app/generate_stdf_inspired_data.py'
            }
        }

        stage('Process STDF-Inspired Data') {
            steps {
                sh 'python3 app/process_stdf_inspired_data.py'
            }
        }

        stage('Validate STDF Reports') {
            steps {
                sh '''
                    test -f data/stdf_inspired_test_records.csv
                    test -f reports/stdf_yield_summary.csv
                    test -f reports/stdf_yield_breakdown.csv
                    test -f reports/stdf_yield_report.txt

                    grep -q "yield_percentage" reports/stdf_yield_summary.csv
                    grep -q "STDF-Inspired Yield Report" reports/stdf_yield_report.txt
                '''
            }
        }

        stage('Run Application Health Checks') {
            steps {
                sh 'python3 app/health_check.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/test_results.csv,dashboard/index.html,reports/health_check_report.txt,data/stdf_inspired_test_records.csv,reports/stdf_yield_summary.csv,reports/stdf_yield_breakdown.csv,reports/stdf_yield_report.txt', fingerprint: true
        }
    }
}
