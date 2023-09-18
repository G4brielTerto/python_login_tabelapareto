import sqlite3
import getpass
import os

banco=sqlite3.connect('banco_sistema.db')
cursor=banco.cursor()

#cursor.execute("CREATE TABLE usuario (nome text, idade integer, email tex)")
#banco.commit()

#cursor.execute("CREATE TABLE usuarios (nome text, idade int, email text, senha)")




def cadastro():
    nome=input("Digite seu nome: ")
    email=input("Digite seu email: ")
    idade=int(input("Digite seu idade: "))
    senha= getpass.getpass("Digite sua senha: ")
    if len(senha) > 20:
        while len(senha) > 20:
            print("SUA SENHA NÃO PODE TER MAIS DO QUE 20 CARACTERES")
            senha= getpass.getpass("Digite sua senha: ")
    cursor.execute("""INSERT INTO usuarios (nome, idade, email, senha) VALUES (?,?,?,?) """, (nome, idade, email, senha))
    banco.commit()
    print("DADOS CADASTRADOS COM SUCESSO!")
    os.system('clear')

def login():
    while True:
        email=input("Digite seu email: ")
        senha=getpass.getpass("Digite sua senha: ")
        cursor.execute("SELECT senha FROM usuarios WHERE email='{}'".format(email))
        senhabd=cursor.fetchall()
        if(senha == senhabd[0][0]):
            sistema_pareto()
        else:
            print("ERRO! Tente novamente")
            print("Caso não tenha se cadastrado digite [1]")
            i=input("Digite algo para continuar:\n")
            if i==1:
                cadastro()

def sistema_pareto():
    a=''
    cont="s"
    lista=[]
    titulo="TABELA DE PARETO"

    while cont=="s":
        print(f'{a:-^80}')
        print(f'{titulo:-^80}')
        print(f'{a:-^80}')
        dados_linhas=[]
        dados_linhas.append(input("Digite um dado: \n"))
        ocorrencias=[]
        ocorrencias.append(input("Digite a ocorrência: \n"))
        cont=input('deseja continuar?\n')
        lista.append(dados_linhas+ocorrencias)

    
    print(f'{a:-^80}')
    for i in lista:
            print(f"|{i[0]:^35}| {i[1]:^35}|")
    print(f'{a:-^80}')



while True:
    print("===================================")
    print("BEM VINDO AO NOSSO SISTEMA!")
    print("===================================")
    print("O que deseja realizar?")
    print("Digite [1] para fazer o cadastro.")
    print("Digite [2] para fazer o login.")
    print("Digite [0] para sair.\n")
    i=int(input(":"))
    if i==0:
        break
    elif i==1:
        cadastro()
    elif i==2:
        login()
