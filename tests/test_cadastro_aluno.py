import sys
sys.path.append('/var/lib/jenkins/workspace/aluno')
<<<<<<< HEAD
sys.path.insert(0, '/usr/local/lib/python3.12/site-packages')
from appflask import app, db, Aluno
=======
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify, Response
from app import app, db, Aluno
>>>>>>> 86bd5a6 (conexão DB)

site_packages_path = site.getsitepackages()[0]
if site_packages_path not in sys.path:
    sys.path.insert(0, site_packages_path)

def client():
    # Configura o app para testes
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco de dados em memória para testes
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Cria as tabelas no banco em memória
        yield client

def test_adicionar_aluno(client):
    # Dados do aluno para o teste
    aluno_data = {
        "nome": "João",
        "sobrenome": "Silva",
        "turma": "3A",
        "disciplinas": "Matemática, Português"
    }

    # Realiza a requisição POST para adicionar o aluno
    response = client.post('/alunos', json=aluno_data)

    # Verifica se o retorno foi um sucesso (status 201)
    assert response.status_code == 201
    assert response.json['message'] == 'Aluno adicionado com sucesso!'

    # Verifica se o aluno foi salvo no banco
    with app.app_context():
        aluno = Aluno.query.filter_by(nome="João", sobrenome="Silva").first()
        assert aluno is not None
        assert aluno.turma == "3A"
        assert aluno.disciplinas == "Matemática, Português"
