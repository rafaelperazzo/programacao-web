# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m = int(input('Digite o valor de m:'))

e = input('digite o valor de epsilon para o cos:')

m = funcoes.CalculoDoValorAbsoluto (m)
PI = funcoes.calculoDoPi(m)
cos = funcoes.CalculoDoCOS(PI/5,e)
razaoAurea=funcoes.CalculoDaRA(m,e)

print ('Valor aproximado de pi: %.15f' %PI)
print ('Valor aproximado da razao aurea: %.15f' %razaoAurea)