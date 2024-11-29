pipeline {
    agent any
    environment {
        IMAGE_REGISTRY = 'jonahirande'
    }

    stages {
        stage ('Deploying '){
            steps {
                sh '''
                kubectl set image deployment/weather-app-deployment weather-app=${IMAGE_REGISTRY}/weather-app-service:1.0 --namespace=default
                kubectl apply -f weather-app/k8s-manifest.yaml
                '''

                // Deploy Dad Jokes App
                sh '''
                kubectl set image deployment/dad-jokes-app-deployment dad-jokes-service=${IMAGE_REGISTRY}/dad-jokes-service:1.0 --namespace=default
                kubectl apply -f dad-jokes/k8s-manifest.yaml
                '''

                // Deploy Fitness Advice App
                sh '''
                kubectl set image deployment/fitness-advice-app-deployment fitness-advice-app=${IMAGE_REGISTRY}/fitness-advice-app:1.0 --namespace=default
                kubectl apply -f fitness-advice/k8s-manifest.yaml
                '''

                // Deploy Guessing Game App
                sh '''
                kubectl set image deployment/guessing-game-app-deployment guessing-game-app=${IMAGE_REGISTRY}/guessing-game-service:1.0 --namespace=default
                kubectl apply -f guessing-game/k8s-manifest.yaml
                '''
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
