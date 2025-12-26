pipeline {
    agent any

    stages {
        stage('Start HTTP Stream Server') {
            steps {
                sh '''
                nohup python mock_servers/http_stream_server.py > server.log 2>&1 &
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
