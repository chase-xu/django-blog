pipeline{
  agent {
    kubernetes {
      defaultContainer 'kaniko'
       yaml '''
        apiVersion: v1
        kind: Deployment
        metadata:
          labels:
            app: webblog
            name: webblog
        spec: 
          replicas: 1
          selector: 
            matchLabels:
              app: webblog
          template:
            metadata:
              labels:
              app: webblog
            spec:
              containers:
              - name: shell
                image: ubuntu
                imagePullPolicy: Always
                name: webblog
       '''
    }
  }
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
        echo 'mid of testing'
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
