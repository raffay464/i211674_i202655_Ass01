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

        stage('Run Tests') {
            when {
                expression { env.BRANCH_NAME == 'test' }
            }
            steps {
                sh '''
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                pytest test.py  # Run test.py explicitly
                '''
            }
        }

        stage('Build & Push Docker Image') {
            when {
                expression { env.BRANCH_NAME == 'main' }
            }
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
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
                    emailext subject: 'Deployment Successful!',
                        body: 'Your ML Flask app has been deployed!',
                        recipientProviders: [[$class: 'DevelopersRecipientProvider']]
                }
            }
        }
    }
}
