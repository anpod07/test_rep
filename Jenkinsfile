pipeline {
    agent { label 'master' }
    options {
        disableConcurrentBuilds()
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '3')
        timestamps()
    }
    stages {
        stage('Hello') {
            steps {
                dir('/var/jenkins_home/workspace') {
                    sh 'ls -la'
                    sh 'sleep 5'
                }
            }
        }
    }
}
