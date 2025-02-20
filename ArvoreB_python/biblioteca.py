#Declaração das classes e definição do grau da árvore

class Registro:
  def __init__(self):
    self.Chave = None
    self.Arquivo = None

class Pagina:
  def __init__(self, ordem):
    self.n = 0
    self.r = [None for i in range(ordem)]
    self.p = [None for i in range(ordem+1)]

#Pesquisa

def Pesquisa(x, Ap):
  i = 1
  if (Ap == None):
    print("Registro não está presente na árvore\n")
    return

  while (i < Ap.n and x.Chave > Ap.r[i - 1].Chave):
    i += 1
  if (x.Chave == Ap.r[i - 1].Chave):
    x = Ap.r[i - 1]
    return x

  if (x.Chave < Ap.r[i - 1].Chave):
    x = Pesquisa(x, Ap.p[i - 1])
  else:
    x = Pesquisa(x, Ap.p[i])
  return x

#Funções de inserção

#Insere o registro na página escolhida
def InsereNaPagina(Ap, Reg, ApDir):
  k = Ap.n
  NaoAchouPosicao = (k > 0)
  while (NaoAchouPosicao):
    if ( Reg.Chave >= Ap.r[k - 1].Chave ):
      NaoAchouPosicao = False
      break
    Ap.r[k] = Ap.r[k - 1]
    Ap.p[k + 1] = Ap.p[k]
    k-= 1
    if (k < 1):
      NaoAchouPosicao = False

  Ap.r[k] = Reg
  Ap.p[k + 1] = ApDir
  Ap.n += 1

#Busca a página onde o registro será inserido e controla a divisão de páginas por Overflow
def Ins( Reg, Ap, Cresceu, RegRetorno, ApRetorno, Ordem ):
  i = 1
  J = None
  if (Ap == None):
    Cresceu = True
    RegRetorno = Reg
    ApRetorno = None
    return Cresceu, RegRetorno, ApRetorno

  while ( i < Ap.n and Reg.Chave > Ap.r[i - 1].Chave ):
    i+= 1

  if(Reg.Chave == Ap.r[i - 1].Chave):
    print(" Erro: Registro já está presente\n")
    Cresceu = False
    return Cresceu, RegRetorno, ApRetorno

  if(Reg.Chave < Ap.r[i - 1].Chave ):
    i-= 1

  Cresceu, RegRetorno, ApRetorno = Ins(Reg, Ap.p[i], Cresceu, RegRetorno, ApRetorno, Ordem)

  if(not Cresceu):
    return Cresceu, RegRetorno, ApRetorno
  if (Ap.n < Ordem): # Página tem espaco
    InsereNaPagina(Ap, RegRetorno, ApRetorno)
    Cresceu = False
    return Cresceu, RegRetorno, ApRetorno

  # Overflow: Página tem que ser dividida /
  ApTemp = Pagina(Ordem)
  ApTemp.n = 0
  ApTemp.p[0] = None
  if (i < (Ordem//2) + 1):
    InsereNaPagina(ApTemp, Ap.r[Ordem - 1], Ap.p[Ordem])
    Ap.n-= 1
    InsereNaPagina(Ap, RegRetorno, ApRetorno)
  else:
    InsereNaPagina(ApTemp, RegRetorno, ApRetorno)
  for J in range((Ordem//2) + 2, Ordem + 1):
    InsereNaPagina(ApTemp, Ap.r[J - 1], Ap.p[J])
  Ap.n = (Ordem//2)
  ApTemp.p[0] = Ap.p[(Ordem//2) + 1]
  RegRetorno = Ap.r[(Ordem//2)]
  ApRetorno = ApTemp
  return Cresceu, RegRetorno, ApRetorno

#Cria página da nova raiz caso a árvore cresça em altura
def Insere(Reg, Ap, Ordem):
  Cresceu = False
  RegRetorno = Registro()
  ApRetorno = Pagina(Ordem)
  Cresceu, RegRetorno, ApRetorno = Ins(Reg, Ap, Cresceu, RegRetorno, ApRetorno, Ordem)
  if (Cresceu):
    ApTemp = Pagina(Ordem)
    ApTemp.n = 1
    ApTemp.r[0] = RegRetorno
    ApTemp.p[1] = ApRetorno
    ApTemp.p[0] = Ap
    Ap = ApTemp
  return Ap

#Define os registros a serem inseridos
def Inserir(Ap):
  ordem = int(input("Digite a ordem da árvore:"))
  chave = int(input("\nDigite uma chave (<= 0 para parar):"))
  while (chave > 0):
    reg = Registro()
    reg.Chave = chave
    arq = input("Digite o nome do arquivo:")
    if arq.lower().endswith(".csv"):
      reg.Arquivo = pd.read_csv(arq)      
    elif arq.lower().endswith((".xls", ".xlsx")):
      reg.Arquivo = pd.read_excel(arq)
    else:
      print ("Arquivo incompatível.")
      continue
    Ap = Insere(reg, Ap, ordem)
    chave = int(input("\nDigite uma chave (<= 0 para parar):"))
  return Ap

#Impressão

def Imprime(Ap):
  if (Ap != None):
    i = 0
    while i < Ap.n:
      Imprime(Ap.p[i])
      print(Ap.r[i].Chave)
      i += 1
    Imprime(Ap.p[i])

def ImprimeMenor(x, Ap):
  if (Ap != None):
    i = 0
    while i < Ap.n:
      ImprimeMenor(x, Ap.p[i])
      if (Ap.r[i].Chave < x.Chave):
        print(Ap.r[i].Chave)
      i += 1
    ImprimeMenor(x, Ap.p[i])

def ImprimeMaior(x, Ap):
  if (Ap != None):
    i = 0
    while i < Ap.n:
      ImprimeMaior(x, Ap.p[i])
      if (Ap.r[i].Chave > x.Chave):
        print(Ap.r[i].Chave)
      i += 1
    ImprimeMaior(x, Ap.p[i])

#Execução

import pandas as pd #pip install pandas
import openpyxl #pip install openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference
import string
Ap = None

#Menu
print("Bem-vindo, o que deseja realizar?")
menu = True
while menu:
  cmd = int(input("\nMenu de opções\n0 - Sair, 1 - Inserir, 2 - Pesquisar, 3 - Imprimir em-ordem, 4 - Imprimir valores menores que uma chave, 5 - Imprimir valores maiores que uma chave.\nOpção:"))
  print("\n")
  
  if cmd == 0:
    print("Programa finalizado. ")
    menu = False
  elif cmd == 1:
    Ap = Inserir(Ap)
  elif cmd == 2:
    reg = Registro()
    reg.Chave = int(input("\nDigite uma chave maior que zero: "))
    reg = Pesquisa(reg, Ap)
  elif cmd == 3:
    Imprime(Ap)
  elif cmd == 4:
    reg = Registro()
    reg.Chave = int(input("\nDigite uma chave maior que zero: "))
    ImprimeMenor(reg, Ap)
  elif cmd == 5:
    reg = Registro()
    reg.Chave = int(input("\nDigite uma chave maior que zero: "))
    ImprimeMaior(reg, Ap)
  else:
    print("Comando inexistente.")
