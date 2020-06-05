pipeline {

    agent any
     options {
          buildDiscarder(logRotator(numToKeepStr: '200'))
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

                echo 'image is build and push'
            }
        }
        stage('Deploy') {
            steps{
                echo " Deploy"
                

            }
        }
    }

}