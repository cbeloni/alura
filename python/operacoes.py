# -*- coding: UTF-8 -*-
# operacoes.py

class Soma(object):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita
    
    def avalia(self):
        return self.__expressao_direita.avalia() + self.__expressao_esquerda.avalia()

    def aceita(self, visitor):
        visitor.visita_soma(self)
  
    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

class Subtracao(object):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita
    
    def avalia(self):
        return (self.__expressao_direita.avalia() - self.__expressao_esquerda.avalia())

    def aceita(self, visitor):
        visitor.visita_subtracao(self)

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

class Numero(object):
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

    def aceita(self, visitor):
        visitor.visita_numero(self)

class Impressora(object):
    """docstring for Impressora"""
    def visita_soma(self, soma):
        print '+(',
        soma.expressao_esquerda.aceita(self)
        soma.expressao_direita.aceita(self)
        print ')',

    def visita_subtracao(self, subtracao):
        print '-(',
        subtracao.expressao_esquerda.aceita(self)
        subtracao.expressao_direita.aceita(self)
        print ')',

    def visita_numero(self, numero):

        print numero.avalia()


if __name__ == '__main__':

    expressao_esquerda = Subtracao(Numero(10), Numero(5))
    expressao_direita = Soma(Numero(2), Numero(10))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)

    resultado = expressao_conta.avalia();
    print resultado

    visitor = Impressora()
    expressao_conta.aceita(visitor)