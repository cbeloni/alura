# -*- coding: utf-8 -*-
from impostos import ISS, ICMS, ICPP, IKCV
from orcamento import Item

class Calculador_de_impostos(object):
    
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)           
        print imposto_calculado
        
if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item("pasta de dentes", 100))
    
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

    #Calculo imposto composto IKCV + ISS
    calculador.realiza_calculo(orcamento, IKCV(ISS(ICMS())))
