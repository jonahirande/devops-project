pipeline {
    agent any
    environment {
        KUBECONFIG_CREDENTIALS_ID = 'kubeconfig' // Replace with your Jenkins credentials ID
        IMAGE_REGISTRY = 'jonahirande'  // Replace with your Docker Hub username or registry
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/jonahirande/devops-project.git'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: KUBECONFIG_CREDENTIALS_ID, variable: 'KUBECONFIG')]) {
                    script {
                        // Deploy Weather App
                        sh """
                        kubectl set image deployment/weather-app-deployment weather-app=${IMAGE_REGISTRY}/weather-app-service:1.0 --namespace=default
                        kubectl apply -f weather/k8s-manifest.yaml
                        """

                        // Deploy Dad Jokes App
                        sh """
                        kubectl set image deployment/dad-jokes-app-deployment dad-jokes-service=${IMAGE_REGISTRY}/dad-jokes-service:1.0 --namespace=default
                        kubectl apply -f dad-jokes-service/k8s-manifest.yaml
                        """

                        // Deploy Fitness Advice App
                        sh """
                        kubectl set image deployment/fitness-advice-app-deployment fitness-advice-app=${IMAGE_REGISTRY}/fitness-advice-app:latest --namespace=default
                        kubectl apply -f fitness-advice-service/k8s-manifest.yaml
                        """

                        // Deploy Guessing Game App
                        sh """
                        kubectl set image deployment/guessing-game-app-deployment guessing-game-app=${IMAGE_REGISTRY}/guessing-game-service:1.0 --namespace=default
                        kubectl apply -f guessing-game-service/k8s-manifest.yaml
                        """
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'Deployment completed successfully!'
        }
        failure {
            echo 'Deployment failed. Check the logs for errors.'
        }
    }
}
