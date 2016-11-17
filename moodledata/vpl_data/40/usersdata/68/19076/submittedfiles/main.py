# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=int(input('Digite m:'))
e=input('Digite o epsilon para o cosseno:')

if m<0:
    m=m*(-1)

funcoes.calculaPi(m)
pi=calculaPi(m)
    
funcoes.calculaCosseno(e)
cosseno=calculaCosseno(pi)
    
funcoes.calculaRazaoAurea(cosseno)
razaoAurea=calculaRazaoAurea(cosseno)
    
print('%.15f' %pi)
print('%.15f' %razaoAurea)