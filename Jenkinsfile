pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {

                checkout scm
                echo ' Code pulled successfully.'
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo '🧪 Running Pytest...'
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pip install pytest httpx  # Added httpx because FastAPI tests need it
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

                sh 'docker stop api-container || true'
                sh 'docker rm api-container || true'


                sh 'docker run -d -p 8000:8000 --name api-container real-estate-api:latest'
                echo '🎉 Deployment Successful! API is live on port 8000.'
            }
        }
    }


    post {
        failure {
            echo ' Pipeline failed! Check the logs.'
        }
    }
}