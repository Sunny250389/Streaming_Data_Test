pipeline {
    agent any

    stages {
        stage('Start HTTP Stream Server') {
            steps {
                sh '''
                python mock_servers/http_stream_server.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}
