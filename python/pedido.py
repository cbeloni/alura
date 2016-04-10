# -*- coding: UTF-8 -*-
# pedido.py
from datetime import date
class Pedido(object):
    """docstring for Pedido"""
    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def pagar(self):
        self.__status = 'PAGO'

    def finalizar(self):
        self.__status = 'ENTREGUE'
        self.__data_finalizacao = date.today()

    @property    
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao

class Fila_de_trabalho(object):

    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()

from abc import ABCMeta, abstractmethod
class Comando(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass

class Finaliza_pedido(Comando):
    """docstring for finaliza_pedido"""
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finalizar()

class Paga_pedido(Comando):
    """docstring for Paga_pedido"""
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.pagar()
        
        

if __name__ == '__main__':
    pedido = Pedido('Caue', 10)
    pedido2 = Pedido('Tom', 20)

    paga_pedido = Paga_pedido(pedido)
    finaliza_pedido2 = Finaliza_pedido(pedido2)

    fila = Fila_de_trabalho()
    fila.adiciona(paga_pedido)
    fila.adiciona(finaliza_pedido2)

    fila.processa()
    
    print pedido.status
    print pedido.data_finalizacao
    print pedido2.status
    print pedido2.data_finalizacao    
    

