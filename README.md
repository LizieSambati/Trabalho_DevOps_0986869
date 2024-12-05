
---

### Trabalho da disciplina Ferramentas DevOps  
### Criação de Ambiente Monitorado com Pipeline CI/CD

---

Aplicação desenvolvida com framework Flask para cadastro e gerenciamento de alunos.  
Com testes automatizados que cadastram aluno a partir de pipeline no Jenkins.  
Monitoramento com análises de logs de acesso por meio do Prometheus e dashboards de acessos no Grafana.  

---
*Ferramentas:*  
- Linux  
- Docker  
- Docker Compose  
- Shell Script   
- Repositório: Git  
- Aplicação: Flask/Web  
- Banco de dados: MariaDB  
- Pipeline: Jenkins  
- Monitoramento: Prometheus/Grafana  

*Portas:*  
3000 = Grafana  
3306 = MariaDB  
5000 = Aplicação  
8080 = Jenkins  
9090 = Prometheus  

 ---

#### *Iniciar aplicação*  
*Limpar e remover todos os containers (caso necessário):*  
`docker stop $(docker ps -aq) && docker rm $(docker ps -aq)`  

*clonar o repositório:*  
`git clone https://github.com/LizieSambati/Trabalho_DevOps_0986869.git`  

*Subir containers:*  
`docker-compose up --build -d`  

Acessar Jenkins http://localhost:8080 para criar nova tarefa do tipo Pipeline com link do projeto: https://github.com/LizieSambati/Trabalho_DevOps_0986869.git  
Acessar Grafana http://localhost:3000 para visualizar dashboards  
*login: admin*  
*password: admin*  

*Parar aplicação:*  
`sudo docker compose down`  

---
