pipeline {
    agent any
    environment {
        IMAGE_REGISTRY = 'jonahirande'
    }

    stages {
        stage ('Deploying '){
            steps {
                sh '''
                kubectl apply -f weather-app/k8s-manifest.yaml
                '''

                // Deploy Dad Jokes App
                sh '''
                kubectl apply -f dad-jokes/k8s-manifest.yaml
                '''

                // Deploy Fitness Advice App
                sh '''
                kubectl apply -f fitness-advice/k8s-manifest.yaml
                '''

                // Deploy Guessing Game App
                sh '''
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
