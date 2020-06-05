pipeline {
    agent any
         triggers {
        githubPush()
        pollSCM 'H/10 * * * *'
    }
environment { 
        DOCKER_HUB_REPO    = "salmanilyas/batch-ecs-example"
        IMAGE_TAG   = "${env.BRANCH_NAME}"
    }
    stages {
        stage('Config') {
            steps {
                
                echo 'replacing value in config file'               
            }
        }
        stage('Build') {
            steps {
                echo 'Build a image for Company ETL'
                sh 'docker build -t $DOCKER_HUB_REPO:$IMAGE_TAG . '
            }
        }
        stage('Push') {
            steps{
                echo 'heloo'
                sh ' docker push $DOCKER_HUB_REPO:$IMAGE_TAG'
                sh 'docker system prune -f'
            }
        }
    }

}