pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Sh pack') {
            steps {
                sh '''
                    ls -la
                    pwd
                    whoami
                '''
            }
        }
    }
}
