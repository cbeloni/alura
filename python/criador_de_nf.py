# -*- coding: UTF-8 -*-
# nota_fiscal.py
from datetime import date
from nota_fiscal import Nota_fiscal, Item    


class Criador_de_nota_fiscal(object):
    
    def __init__(self):    
        self.__razao_social= None
        self.__cnpj = None
        self.__itens = None
        self.__detalhes = None
        self.__data_de_emissao = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self,cnpj):
        self.__cnpj = cnpj
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_detalhes(self,detalhes):
        self.__detalhes = detalhes
        return self

    def contruir(self):

        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()

        if self.__detalhes is None:
            self.__detalhes = ''

        return Nota_fiscal(razao_social = self.__razao_social, 
                           cnpj = self.__cnpj, 
                           itens = self.__itens,
                           data_de_emissao = self.__data_de_emissao,
                           detalhes = self.__detalhes)

if __name__ == '__main__':

    itens = [Item('borracha',1),
             Item('lapiz',2)]

    nota_fiscal_com_builder = (Criador_de_nota_fiscal()
                              .com_razao_social(29817237192)
                              .com_cnpj(231937182)
                              .com_itens(itens)
                              .contruir())