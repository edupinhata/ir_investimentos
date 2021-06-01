#!/usr/bin/env python3
from transacoes import TipoTransacao
from operator import itemgetter

class Acao:

  def __init__(self, nome, codigo, cnpj, tipo, codigoIR):
    self.nome  = nome 
    self.codigo = codigo
    self.cnpj = cnpj
    self.tipo = tipo
    self.codigoIR = codigoIR
    self.transacoes = []
    acoes_output_str = "7 ACOES DE MAHLE METAL LEVE SA, COM CODIGO DE NEGOCIACAO LEVE3. CUSTO COTAL: R$169,82"
    fii_output_str = "15 COTAS DE CSHG Renda Urbana, COM CODIGO DE NEGOCIACAO HGRU11. CUSTO TOTAL: R$582,80"


  def __str__(self):
    return "%s (%s). Tipo: %s" % (self.nome, self.codigo, self.codigoIR)

  def GetQuantidadeValorMedio(self, maxDate):
    numAcoesPeriodo = 0
    valorMedioAcoesPeriodo = 0
    self.transacoes.sort(key=lambda x: x.data, reverse=False)

    for trans in self.transacoes:
      if trans.data <= maxDate:
        if trans.tipo == TipoTransacao.COMPRA:
          valorTotalMedioPeriodo = valorMedioAcoesPeriodo * numAcoesPeriodo
          numAcoesPeriodo += trans.quantidade
          valorMedioAcoesPeriodo = (valorTotalMedioPeriodo + trans.valorTotal) / numAcoesPeriodo
        elif trans.tipo == TipoTransacao.VENDA:
          numAcoesPeriodo += trans.quantidade

    return numAcoesPeriodo, valorMedioAcoesPeriodo

  def GetIROutput(self, maxDate):
    str_saida = ""

    quantidade, valorMedio = self.GetQuantidadeValorMedio(maxDate)

    str_saida += self.codigo + "\n"
    str_saida += self.cnpj + "\n"
    str_saida += "CodigoIR: " + self.codigoIR + "\n"
    str_saida += "%s AÇÕES DE %s, COM CÓDIGO DE NEGOCIAÇÃO %s. CUSTO TOTAL: R$%.2f.\n" % (quantidade,
    self.nome, self.codigo, valorMedio*quantidade) 
    str_saida += "==========================="

    return str_saida

    
