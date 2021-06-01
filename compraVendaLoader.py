#!/usr/env/bin python3
from acao import Acao
from transacoes import Transacoes
from transacoes import TipoTransacao

class CompraVendaLoader:

  def __init__(self, trans_path, acoes_info_path):
    self.acoes = {} 
    self.LoadAcoesInfo(acoes_info_path)
    self.LoadTransacoes(trans_path)

  def LoadAcoesInfo(self, acoes_info_path, ignoreHeader=True):
    count = 0
    try:
      with open(acoes_info_path, "r") as file:
        for line in file:
          if (ignoreHeader and count == 0):
            count += 1
            continue
          splitLine = line.split(",")
          codigo = splitLine[0]
          tipo = splitLine[1]
          cnpj = splitLine[2]
          nome = splitLine[3]
          codigoIR = splitLine[4]
          if codigo not in self.acoes:
            self.acoes[codigo] = Acao(nome, codigo, cnpj, tipo, codigoIR)
    except:
      print("Error: could not read acoes info from %s." % acoes_info_path)

  def LoadTransacoes(self, trans_path, ignoreHeader=True):
    count = 0
    lines = []
    try:
      with open(trans_path, "r") as file:
        for line in file:
          if (ignoreHeader and count == 0):
            count += 1
            continue
          lines.append(line)

    except:
      print("Error while reading %s." % (trans_path))

    for line in lines:
      self.processLine(line)

  def processLine(self, line):
    splitLine = line.split(",")
    if (splitLine[0] == ""):
      return
  
    codigo = splitLine[0]
    data = splitLine[2]
    valorUnitario = float(splitLine[3])
    quantidade = int(splitLine[4])
    tipo = TipoTransacao.COMPRA if quantidade > 0 else TipoTransacao.VENDA

    if codigo not in self.acoes:
      self.acoes[codigo] = Acao("", codigo, "", tipo, "")  
    transacao = Transacoes(codigo, data, tipo, valorUnitario, quantidade)
    self.acoes[codigo].transacoes.append(transacao)
