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
                    branches: [[name: '*/main']],  
                    userRemoteConfigs: [[
                        url: 'https://github.com/ahmadusama974/i211674_i202655_Ass01.git'
                    ]]
                ])
                script {
                    echo "Detected branch: ${env.GIT_BRANCH}"
                }
            }
        }

        stage('Build & Push Docker Image') {
            when {
                expression { env.GIT_BRANCH.endsWith('main') }  
            }
            steps {
                script {
                    echo "Building Docker image..."
                    bat 'docker build -t %DOCKER_IMAGE% .'   //  Fixed variable format
                    
                    echo "Pushing Docker image to Docker Hub..."
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                        bat 'docker push %DOCKER_IMAGE%'   //  Fixed variable format
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                def BUILD_STATUS = currentBuild.currentResult ?: 'UNKNOWN'
                echo "Sending email notification... (Status: ${BUILD_STATUS})"

                emailext(
                    subject: "Jenkins Build: ${BUILD_STATUS}",
                    body: """
                    <p><strong>Pipeline Status:</strong> ${BUILD_STATUS}</p>
                    <ul>
                        <li>✅ <a href="https://github.com/ahmadusama974/i211674_i202655_Ass01">GitHub Repo</a></li>
                        <li>✅ <a href="https://hub.docker.com/repository/docker/ahmadusama20i2655/flask-ml-app">Docker Hub Image</a></li>
                    </ul>
                    <p>Regards,<br>Jenkins CI/CD</p>
                    """,
                    mimeType: 'text/html',
                    to: 'agkraffay01@gmail.com'
                )
            }
        }
    }


}
