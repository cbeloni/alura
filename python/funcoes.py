def gera_nome_convite(nome):
  convite = nome
  posicao_final = len(convite)
  posicao_inicial = posicao_final - 4
  parte1 = convite[0:4]
  parte2 = convite[posicao_inicial:posicao_final]
  return ("%s %s") % (parte1, parte2)

def envia_convite(nome_formatado):
    print ("Enviado convite para ") + nome_formatado

def processa_convite(nome):
    envia_convite(gera_nome_convite(nome))

nomes = []
def cadastrar(nome):
   nomes.append(nome)    

def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)   

