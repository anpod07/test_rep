pipeline {
    agent { label 'master' }
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '3')
        disableConcurrentBuilds()
        timestamps()
    }
    triggers { pollSCM '* * * * *' }
    stages {
        stage('Hello') {
            steps {
                dir('/var/jenkins_home/workspace') {
                    sh 'ls -la'
                }
            }
        }
    }
}
