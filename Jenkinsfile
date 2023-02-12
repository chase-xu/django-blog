pipeline{
  agent any
  parameters {
    booleanParam(name: 'executeTests', defaultValue: true, description:'')
    booleanParam(name: 'executeBuild', defaultValue: true, description:'')
    booleanParam(name: 'executeDeploy', defaultValue: true, description:'')
  }
  triggers {
    githubPush()
  }
  stages{
    stage('build'){
      steps{
        script{
          result = sh(script: 'docker-compose up', returnStdout: true).trim()
          println(result)
        }
      }
    }
    stage('post build'){
      steps{
        
      }
    }
  } 
}
