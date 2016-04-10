# -*- coding: UTF-8 -*-
# contrato.py

from datetime import date

class Contrato(object):

    def __init__(self, cliente, data, tipo = 'NOVO'):
        self.__cliente = cliente
        self.__data = data
        self.__tipo = tipo
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
    
    def avanca(self):
        if self.__tipo == 'NOVO':
            self.__tipo = 'EM ANDAMENTO'
        elif self.__tipo == 'EM ANDAMENTO':
            self.__tipo = 'ACERTADO'
        elif self.__tipo == 'ACERTADO': 
            self.__tipo = 'CONCLUIDO'
    
    def salva_estado(self):
        return Contrato(self.__cliente, self.__data, self.__tipo)

class Estado(object):
    """docstring for Estado"""
    def __init__(self, contrato):
        self.__contrato = contrato

    @property
    def contrato(self):
        return self.__contrato

class Historico(object):

    def __init__(self):
        self.__lista_estados = []

    def adiciona_estado(self,estado):
        self.__lista_estados.append(estado)

    @property
    def lista_estados(self):
        return self.__lista_estados

                        

if __name__ == '__main__':
    historico = Historico()

    contrato = Contrato(data=date.today() ,cliente='Flávio Almeida')

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    for i in historico.lista_estados:
        print i.tipo
