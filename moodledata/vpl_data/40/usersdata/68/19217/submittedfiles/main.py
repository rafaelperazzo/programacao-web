# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m=int(input('Digite m:'))
e=input('Digite o epsilon para o cosseno:')

m= funcoes.calculaValorAbsoluto (m)

pi=funcoes.calculaPi(m)

cosseno=funcoes.calculaCosseno(pi/5,e)

razaoAurea=funcoes.calculaRazaoAurea(m,e)

print('%.15f' %pi)
print('%.15f' %razaoAurea)