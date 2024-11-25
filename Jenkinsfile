pipeline {
    agent any

    stages {
        stage('check') {
            steps {
			echo 'subindo a aplicação'
                }
        }

	stage('git') {
		steps {
			script {
			sh 'rm -rf Trabalho_DevOps_0986869'
			sh 'git clone https://github.com/LizieSambati/Trabalho_DevOps_0986869.git'
			dir('Trabalho_DevOps_0986869') {
				sh 'git checkout main'
                    }
                }
            }
        }

        stage('build inicial') {
            steps {
                script {
			echo 'build inicial'
                }
            }
        }

        stage('testes') {
            steps {
                script {
			echo 'testes'
                }
            }
        }

        stage('build') {
            steps {
                script {
			echo 'build'
                }
            }
        }

        stage('subindo ambiente') {
            steps {
                script {
			echo 'subindo o ambiente'
                }
            }
        }

        stage('deploy ambiente') {
            steps {
                script {
			echo 'deploy ambiente'
                }
            }
        }
    }
}
