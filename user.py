import db_connect

def cadastrar():
    nome=input("insira o nome: ")
    sobrenome=input("insira o sobrenome: ")
    email=input("insira o email:")
    matricula=input("Insira sua matrícula: ")
    cpf=input("Insira seu CPF: ")

    db_connect.cadastrar(nome, sobrenome, email, matricula, cpf)

