import psycopg2

dbname="contracheque"
user="postgres"
password="jesus.cristo"
host="localhost"
port="5432"

try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    print('Conexão ao PostgreSQL bem-sucedida!')
except psycopg2.Error as e:
    print('Erro ao conectar ao PostgreSQL:', e)

def cadastrar(nome, sobrenome, email, matricula, cpf):
    cursor = conn.cursor()

    cursor.execute('INSERT INTO funcionario (nome, sobrenome, email, matricula, cpf) VALUES (%s, %s, %s, %s, %s)', (nome, sobrenome, email, matricula, cpf))
    conn.commit()
    print(f"Cadastro de {nome} feito com sucesso!")
