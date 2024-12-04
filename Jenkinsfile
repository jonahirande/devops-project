pipeline {
    agent any
    environment {
        IMAGE_REGISTRY = 'jonahirande'
    }

    stages {
        stage ('Deploying '){
            steps {
                sh '''
                kubectl apply -f ./weather-app/k8s-manifest.yaml
                '''

                // Deploy Dad Jokes App
                sh '''
                kubectl apply -f ./dad-jokes/k8s-manifest.yaml
                '''

                // Deploy Fitness Advice App
                sh '''
                kubectl apply -f ./fitness/k8s-manifest.yaml
                '''

                // Deploy Guessing Game App
                sh '''
                kubectl apply -f ./guessing-game/k8s-manifest.yaml
                '''

                // Deploy Nginx service
                sh '''
                kubectl apply -f ./other-microservices/nginx.yaml
                '''

                // Deploy Busybox
                sh '''
                kubectl apply -f ./other-microservices/busybox.yaml
                '''

                // Deploy the Sample Voting App from Docker hub
                sh '''
                kubectl apply -f ./k8s-specifications/
                '''

                // Set up helm repo for Grafana
                sh '''
                helm repo add grafana https://grafana.github.io/helm-charts
                helm repo update
                '''

                // Deploy Grafana via helm
                sh '''
                helm upgrade --install grafana grafana/grafana --namespace monitoring --create-namespace \
                --set service.type=NodePort --set adminPassword=irande --set service.port=32005
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
