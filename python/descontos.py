# -*- coding: UTF-8 -*-
# descontos.py
class Desconto_por_cinco_itens(object):
  def __init__ (self, proximo_desconto):
    self.__proximo_desconto = proximo_desconto

  def calcular(self, orcamento):

    if(orcamento.total_itens > 5):
        print 'por total itens'
        return orcamento.valor * 0.1
    else: 
      # se não segue a regra, o desconto é zero!
      return self.__proximo_desconto.calcular(orcamento)

class Desconto_por_mais_de_quinhentos_reais(object):
  def __init__(self,proximo_desconto):
    self.__proximo_desconto = proximo_desconto

  def calcular(self,orcamento):

    if(orcamento.valor > 500):
      print 'por quinhentos'
      return orcamento.valor * 0.07
    else:
      # se não segue a regra, o desconto é zero
      return self.__proximo_desconto.calcular(orcamento)

class Desconto_por_cem_reais(object):
  def __init__(self,proximo_desconto):
    self.__proximo_desconto = proximo_desconto

  def calcular(self,orcamento):

    if(orcamento.valor == 100):
      print 'por cem'
      return orcamento.valor * 0.10
    else:
      return self.__proximo_desconto.calcular(orcamento)

class Sem_desconto(object):

  def calcular(self,orcamento):
    return 0