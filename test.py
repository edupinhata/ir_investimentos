#!/usr/bin/env python3
import datetime
from transacoes import Transacoes
from transacoes import TipoTransacao
from acao import Acao
from compraVendaLoader import CompraVendaLoader


end_of_2020 = datetime.datetime(2020, 12, 31)

def testTransacoes():
  transacoes = []
  transacoes.append(Transacoes("GOL4", datetime.datetime(2020, 5, 17), TipoTransacao.COMPRA, 5, 10))
  print(transacoes[0])

def testLoader():
  cvl = CompraVendaLoader("compra_venda_2021.csv", "acoes_info.csv")
  for acao in cvl.acoes:
    print(cvl.acoes[acao].GetIROutput(end_of_2020))

testLoader()



