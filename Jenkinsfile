pipeline {
    agent any

    stages {
        stage('Start HTTP Stream Server') {
            steps {
                bat 'python mock_servers\\http_stream_server.py'
            }
        }
    }
}
