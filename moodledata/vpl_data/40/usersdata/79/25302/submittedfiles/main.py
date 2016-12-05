# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m = int(input('Digite o valor de m:'))

e = input('digite o valor de epsilon para o cos:')

m = funcoes.CalcValorAbsoluto(m)
PI = funcoes.calculoDopi(m)
cos = funcoes.CCOS(PI/5,e)
razaoAurea=funcoes.CRA(m,e)

print ('Valor aproximado de pi: %.15f' %pi)
print ('Valor aproximado da razao aurea: %.15f' %razaoAurea)