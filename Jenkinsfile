pipeline {
    agent any

    stages {
        stage('check') {
            steps {
			    echo 'E aeeeee!'
            }
        }

	    stage('git') {
		    steps {
                script {
                    echo 'Carregando git...'
                    sh 'rm -rf Trabalho_DevOps_0986869'
                    sh 'git clone https://github.com/LizieSambati/Trabalho_DevOps_0986869.git'
                    dir('Trabalho_DevOps_0986869') {
                        sh 'git checkout main'
                    }
                }
            }
        }

        stage('build Inicial') {
            steps {
                script {
                    echo 'Executando build inicial...'
                    dir("${WORKSPACE}") {
                        sh 'docker-compose down'
                        sh 'docker-compose up --build -d'
                    }
                }    
            }
        }

        stage('testes') {
            steps {
                script {
                    echo 'Executando testes...'
                    dir("${WORKSPACE}") {
                        echo 'Teste cadastro aluno'
                        sh '''
                        if [ ! -d "venv" ]; then
                            python3 -m venv venv
                        fi
                        . venv/bin/activate
                        export PYTHONPATH=$PYTHONPATH:${WORKSPACE}
                        pip install -r flask/requirements.txt
                        pytest tests/test_cadastro_aluno.py --maxfail=1 --disable-warnings
                        '''
                    }
                }
            }
        }


        stage('build') {
            steps {
                script {
			        echo 'build...'
                }
            }
        }

        stage('subindo ambiente') {
            steps {
                script {
			        echo 'Subindo o ambiente...'
                }
            }
        }

        stage('deploy ambiente') {
            steps {
                script {
			        echo 'deploy ambiente!'
                }
            }
        }
    }
}
