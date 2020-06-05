pipeline {

    agent any
    
         triggers {
        githubPush()
        pollSCM 'H/10 * * * *'
    }

environment { 

        DOCKER_HUB_REPO    = "salmanilyas/flask_image"
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
                echo  " This Branch is got Changed ${env.BRANCH_NAME}" 

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