# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m = int(input('Digite o valor de m:'))

e = input('digite o valor de epsilon para o cos:')

m = funcoes.CVA (m)
pi = funcoes.CPI(m)
cos = funcoes.CCOS(pi/5,e)
razaoAurea=funcoes.CRA(m,e)

print ('%.15f' %pi)