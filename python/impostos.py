# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Imposto(object):
    
    __metaclass__ = ABCMeta

    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento): pass        

    
class template_impostos(Imposto):
    
    def calcula(self, orcamento):
        if self.deve_usar_maior_taxacao(orcamento):
            return self.regra_imposto_maior(orcamento)
        else:
            return self.regra_imposto_menor(orcamento)

    @abstractmethod
    def deve_usar_maior_taxacao (self, orcamento): pass

    @abstractmethod    
    def regra_imposto_maior(self, orcamento): pass

    @abstractmethod
    def regra_imposto_menor(self, orcamento): pass



class ISS(Imposto):
        
    def calcula(self,orcamento):
        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)

class ICMS(Imposto):
                        
    def calcula(self,orcamento):
        return orcamento.valor * 0.6 + self.calculo_do_outro_imposto(orcamento)

class ICPP(template_impostos):

    def deve_usar_maior_taxacao(self, orcamento):
        return orcamento.valor > 500 

    def regra_imposto_maior(self, orcamento):
        return orcamento.valor * 0.07 + self.calculo_do_outro_imposto(orcamento)

    def regra_imposto_menor(self, orcamento):
        return orcamento.valor * 0.05 + self.calculo_do_outro_imposto(orcamento)

class IKCV(template_impostos):

    def deve_usar_maior_taxacao (self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def regra_imposto_maior(self , orcamento):
        return orcamento.valor * 0.10 + self.calculo_do_outro_imposto(orcamento)

    def regra_imposto_menor(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)

    def __tem_item_maior_que_100_reais(orcamento):
        for item in orcamento.obter_itens():
            if(item.valor > 100):
                return True
            return False                        