pipeline{
  agent any
  triggers {
    githubPush()
  }
  stages{
    stage('build'){
      steps{
        echo "building the application..."
        echo "finished building"
      }
    }
    stage('test'){
      steps{
        echo 'testing the application...'
        echo 'mid of testing'
        echo 'finished testing'
      }
    }
    stage('deploy'){
      steps{
        echo 'deploying the application...'
        echo 'finished deploying'
      }
    }
  } 
}
