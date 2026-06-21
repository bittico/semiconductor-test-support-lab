pipeline {
    agent any

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
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/test_results.csv', fingerprint: true
        }
    }
}
