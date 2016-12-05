# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m = int(input('Digite o valor de m:'))
e = input('digite E para o Cos:')
m = funcoes.CalculoDoValorAbsoluto (m)
PI = funcoes.calculoDoPi(m)
cos = funcoes.CalculoDoCOS(PI/5,e)
razaoAurea=funcoes.CalculoDaRA(m,e)

print ('pi: %.15f' %PI)
print ('razao aurea: %.15f' %razaoAurea)