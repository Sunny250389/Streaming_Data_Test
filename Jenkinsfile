pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {

        stage('Verify Python') {
            steps {
                bat '''
                python --version
                pip --version
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '''
                if not exist %VENV_DIR% (
                    python -m venv %VENV_DIR%
                )
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Start HTTP Stream Server') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                start /B python mock_servers\\http_stream_server.py
                '''
            }
        }

        stage('Wait for Server') {
            steps {
                bat 'ping 127.0.0.1 -n 6 > nul'
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                pytest tests
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up background processes'
            bat 'taskkill /IM python.exe /F || exit 0'
        }
    }
}