pipeline{
  agent any
  parameters {
  }
  triggers {
    githubPush()
  }
  stages{
    stage('build'){
      steps{
        script{
          println("building....")
          result = sh(script: 'docker-compose up', returnStdout: true).trim()
          println(result)
        }
      }
    }
    stage('post build'){
      steps{
        script{
          println("post build")
        }
      }
    }
  } 
}
