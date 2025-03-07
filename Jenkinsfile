pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ahmadusama20i2655/flask-ml-app'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: "${env.BRANCH_NAME}", url: 'https://github.com/ahmadusama974/i211674_i202655_Ass01.git'
            }
        }

        stage('Run Tests') {
            when {
                branch 'test'  // Only run tests on the test branch
            }
            steps {
                sh '''
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                pytest
                '''
            }
        }

        stage('Build & Push Docker Image') {
            when {
                branch 'main'  // Only deploy if code is in main
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
