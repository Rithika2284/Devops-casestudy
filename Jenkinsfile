pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'vemularithika7/quote-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/Rithika2284/quote-of-the-day.git', 
                    credentialsId: 'github-creds'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-login', 
                                                  usernameVariable: 'DOCKER_USERNAME', 
                                                  passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "vemularithika7" --password-stdin
                        docker push $DOCKER_IMAGE:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl apply -f deployment.yaml
                    kubectl apply -f service.yaml
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed!'
        }
    }
}
