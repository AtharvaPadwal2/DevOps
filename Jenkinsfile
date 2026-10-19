
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Application') {
            steps {
                dir('DevOps_Practical_3') {
                    sh 'python3 app.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('DevOps_Practical_3') {
                    sh 'docker build -t devops-practical-3 .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run --rm devops-practical-3'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}
