import sqlite3
import getpass
import os
import statistics
import numpy



banco=sqlite3.connect('banco_sistema.db')
cursor=banco.cursor()


# cursor.execute("CREATE TABLE usuarios (nome text, idade int, email text, senha)")




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
    cont="sim"
    titulo="TABELA DE PARETO"
    
    print("")
    print(f'{a:-^80}')
    print(f'{titulo:-^80}')
    print(f'{a:-^80}')
    print("")

    
    dado=[]
    ocorrencias=[]
    ocor=[]

    while cont=="sim":
        dado.append(input("Digite uma ocorrência: \n"))
        var=input("Digite o número de ocorrências: \n")
        ocor.append(var)
        ocorrencias.append(int(var))
        # print(ocorrencias)
        cont=input('deseja continuar?(Digite [sim] ou [nao])\n')
        if cont != "sim" and cont != "nao":
            print("Erro!!! Digite as respostas corretas!")
            print("")
            cont="sim"
        # print(ocorrencias)
    if cont=="nao":
        print("")
        print(f'{a:-^80}')
        print(f'{titulo:^80}')
        print(f'{a:-^80}')
        for i in range(0,len(dado)):
                print(f"|{dado[i] [0]:^35}| {ocor[i] [0]:^35}|")
        print(f'{a:-^80}')
        print("")
        print("")
        


        maior=max(ocorrencias)
        menor=min(ocorrencias)
        ampli=maior-menor
        media=statistics.mean(ocorrencias)
        mediana = statistics.median(ocorrencias)
        moda = statistics.mode(ocorrencias)
        quartil1=numpy.quantile(ocorrencias, 0.25)
        quartil2=numpy.quantile(ocorrencias, 0.5)
        quartil3=numpy.quantile(ocorrencias, 0.75)
        iqr=quartil3-quartil1
        variancia=numpy.var(ocorrencias)
        dp=numpy.std(ocorrencias)
            
        print("\n")
        print("MAIOR valor: ",maior)
        print("MENOR valor: ",menor)
        print("AMPLITUDE: ",ampli)
        print("A MÉDIA é: ",media)
        print("A MEDIANA é: ",mediana)
        print("A MODA é: ",moda)
        print("o 1ºQUARTIL é: ",quartil1)
        print("o 2ºQUARTIL é: ",quartil2)
        print("o 3ºQUARTIL é: ",quartil3)
        print("o IQR é: ",iqr)
        print("O total de variância é de: ",variancia)
        print("O total do desvio padrão é de: ",dp)
        print("")


        print("O que deseja realizar?")
        print("Digite [1] para voltar a tela inicial.")
        print("Digite [0] para sair.\n")
        c=int(input(":"))
        if c==0:
            print("VOCÊ SAIU DO SISTEMA!!!")
            exit()
        elif c==1:
            tela_inicio()
    

def tela_inicio():
    while True:
        print("===================================")
        print("BEM VINDO AO NOSSO SISTEMA!")
        print("===================================")
        print("O que deseja realizar?")
        print("Digite [1] para fazer o cadastro.")
        print("Digite [2] para fazer o login.")
        print("Digite [0] para sair.\n")
        c=int(input(":"))
        if c==0:
            exit()
        elif c==1:
            cadastro()
        elif c==2:
            login()

tela_inicio()
