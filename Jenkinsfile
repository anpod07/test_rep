ypipeline {
    agent {
        label 'master'
    }
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '3')
        disableConcurrentBuilds()
        timestamps()
    }
    stages {
        stage('Hello') {
            steps {
                sh 'grep \'jenkins\' /etc/group'
                dir('/var/jenkins_home/workspace') {
                    sh '''
                        pwd
                        ls -la
                    '''
                }
            }
        }
    }
}
