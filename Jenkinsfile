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
                sh 'docker build -t $DOCKER_HUB_REPO:$IMAGE_TAG_${env.BUILD_ID} .'
                echo 'image is build and pushinggggg'
            }
        }
        stage('Deploy') {
            steps{
                echo " Deploy"
                

            }
        }
    }

}