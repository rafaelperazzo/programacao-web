# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=int(input('Digite m:'))
e=input('Digite o epsilon para o cosseno:')

if m<0:
    m=m*(-1)

pi=funcoes.calculaPi(m)

cosseno=funcoes.calculaCosseno(pi)

razaoAurea=funcoes.calculaRazaoAurea(cosseno)

print('%.15f' %pi)
print('%.15f' %razaoAurea)