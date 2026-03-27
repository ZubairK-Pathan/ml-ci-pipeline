pipeline {
    // This tells Jenkins it can run on your local Mac's Jenkins setup
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Jenkins automatically pulls the latest code from your Git branch
                checkout scm
                echo '✅ Code pulled successfully.'
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo '🧪 Running Pytest...'
                // We create a temporary virtual environment to run tests safely
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                pytest test_main.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building the new Docker image...'
                sh 'docker build -t real-estate-api:latest .'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo '🚀 Deploying the container...'
                // 1. Stop and remove the old container if it exists
                sh 'docker stop api-container || true'
                sh 'docker rm api-container || true'

                // 2. Run the new, updated container in the background (-d)
                sh 'docker run -d -p 8000:8000 --name api-container real-estate-api:latest'
                echo '🎉 Deployment Successful! API is live on port 8000.'
            }
        }
    }

    // This section runs after the pipeline finishes, whether it succeeds or fails
    post {
        failure {
            echo '❌ Pipeline failed! Check the logs.'
        }
    }
}