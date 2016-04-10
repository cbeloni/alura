# -*- coding: UTF-8 -*-
# calculador_de_descontos.py
from descontos import Desconto_por_cinco_itens,Desconto_por_mais_de_quinhentos_reais,Desconto_por_cem_reais,Sem_desconto

class Calculador_de_descontos(object):

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(
                   Desconto_por_cem_reais(
                   Desconto_por_mais_de_quinhentos_reais(
                   Sem_desconto()))).calcular(orcamento)

        return desconto

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 30.0))

    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print 'Desconto calculado : %s' % (desconto)