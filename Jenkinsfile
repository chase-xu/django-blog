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
      when{
        expression{
          params.executeBuild
        }
      }

      steps{
        echo "building the application..."
        scripts{
          def customImage = docker.build("webblog:latest")
        }
        echo "finished building"
      }
    }
    stage('test'){
      when {
        expression {
          params.executeTests
        }
      }

      steps{
        echo 'testing the application...'
        scripts {
          customImage.inside {
            sh "python3 manage.py runserver" 
          }
          customImage.push()
        }
        echo 'finished testing'
      }
    }
    stage('deploy'){
      when {
        expression {
          params.executeDeploy
        }
      }
      steps{
        echo 'deploying the application...'
        echo 'finished deploying'
      }
    }
  } 
}
