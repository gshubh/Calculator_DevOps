pipeline {
  environment {
    registry = "guptashubh/calculator"
    registryCredential = 'gshubh'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Building image') {
      steps{
        script {
          dockerImage = sudo docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          sudo docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "sudo docker rmi $registry:$BUILD_NUMBER"
      }
    }
  }
}
