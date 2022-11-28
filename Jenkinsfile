pipeline {

  agent any
  parameters {
    booleanParam(name: 'executeTests', defaultValue: true, description:'')
    booleanParam(name: 'executeBuild', defaultValue: true, description:'')
    booleanParam(name: 'executeDeploy', defaultValue: true, description:'')
  }
  stages{
    stage('build') {
      when{
        expression{
          params.executeBuild
        }
      }
      steps{
        echo "building ..."
        script{
          withCredentials([
              string(
                credentialsId: 'BLOG_SECRET_KEY',
                variable: 'SK')
          ]) {
            docker.withRegistry('', 'docker'){
                def img = docker.build('chaseatdocker/web-blog:latest', "--build-arg SECRET_KEY='${SK}' ./")
                img.push()
            }
          }
        }
      }
    }
    stage('test'){
      when{
        expression{
          params.executeTests
        }
      }
      steps{
        echo "testing ..."
      }
    }
    stage('deploy'){
      when{
        expression{
          params.executeDeploy
        }
      }
      steps{
        echo "deploying ..."
        echo "starting docker container"
        sh 'docker-compose -f compose.yml up -d'
        echo "dcoker container started"
        echo "finished deploying"
      }
    }
  }
}