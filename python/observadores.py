# -*- coding: UTF-8 -*-
# observadores.py

def envia_por_email(nota_fiscal):
    print 'enviando nota do cnpj %s por e-mail' % (nota_fiscal.cnpj)

def salva_no_banco(nota_fiscal):
    print 'salvando no banco nota do cnpj %s' % (nota_fiscal.cnpj)

def imprime(nota_fiscal):
    print 'imprimindo nota do cnpj %s' % (nota_fiscal.cnpj)