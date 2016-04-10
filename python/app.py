# -*- coding: utf-8 -*-
#arquivo app.py

def listar(nomes):
    for nome in nomes:
        print (nome)

def cadastrar(nomes):
    print ('Digite o nome')
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def menu():
    nomes = []
    escolha = ''
    while (escolha != '0'):
        print ('Digite 1 para cadastrar, 2 para lista ou 0 para sair--->')
        escolha = raw_input()
        if(escolha == '1'):
            cadastrar(nomes)
        if (escolha == '2'):
            listar(nomes)
menu()