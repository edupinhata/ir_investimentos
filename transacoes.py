#!/usr/env/bin python3
from enum import Enum
import datetime

class TipoTransacao(Enum):
  COMPRA = 1
  VENDA = 2

class Transacoes:

  def __init__(self, codigo, data, tipo, valorUnitario, quantidade):
    self.codigo = codigo
    self.data = self.getData(data)
    self.tipo = tipo
    self.valorUnitario = valorUnitario
    self.quantidade = quantidade
    self.valorTotal = quantidade * valorUnitario

  def __str__(self):
    return "%s acoes de %s pelo valor de %s. Total: R$ %d" % (self.quantidade, self.codigo,
    self.valorUnitario, self.valorTotal)

  def getData(self, data):
    dataSplit = data.split("/")
    if (len(dataSplit) == 3):
      dia = int(dataSplit[0])
      mes = int(dataSplit[1])
      ano = int(dataSplit[2])
      dataFormated = datetime.datetime(ano, mes, dia)
      return dataFormated
    else:
      print("Erro ao tentar conseguir data de transacao. Data: %s" % data)
      return datetime.datetime(0, 0, 0)
