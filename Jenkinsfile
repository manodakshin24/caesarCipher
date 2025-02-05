pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/manodakshin24/caesarCipher'
            }
        }

        stage('Run Script') {
            steps {
                // Command to run your caesarCipher.py script
                sh 'python caesarCipher.py'
            }
        }

        stage('Post-build Actions') {
            steps {
                // Additional steps to run after the script execution (e.g., publish results, clean up, etc.)
                archiveArtifacts artifacts: '**/output/**', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            deleteDir()
        }
    }
}
