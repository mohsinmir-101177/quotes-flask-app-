pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Deploy Application') {
            steps {
                // Purane containers aur orphaned containers ko clean karein
                sh 'docker-compose down --remove-orphans'
                sh 'docker-compose up -d'
            }
        }
    }
}