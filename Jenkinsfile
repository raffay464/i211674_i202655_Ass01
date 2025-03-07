pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ahmadusama20i2655/flask-ml-app'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "${env.BRANCH_NAME}"]],
                    userRemoteConfigs: [[
                        url: 'https://github.com/ahmadusama974/i211674_i202655_Ass01.git'
                    ]]
                ])
            }
        }

        stage('Build & Push Docker Image') {
            when {
                branch 'main'  // This ensures deployment only happens when merged to main
            }
            steps {
                script {
                    echo "Building Docker image..."
                    sh 'docker build -t $DOCKER_IMAGE .'

                    echo "Pushing Docker image to Docker Hub..."
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }
    }

    post {
        success {
            script {
                if (env.BRANCH_NAME == 'main') {
                    echo "Deployment successful! Sending notification..."
                    emailext subject: 'Deployment Successful!',
                        body: 'Your ML Flask app has been successfully deployed!',
                        recipientProviders: [[$class: 'DevelopersRecipientProvider']]
                }
            }
        }
    }
}
