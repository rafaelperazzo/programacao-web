# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m=int(input('Digite m:'))
e=input('Digite o epsilon para o cosseno:')


#DOUBLE CALCULA_CO_SENO:
soma_cosseno=0
j=2

while i<m and soma_cosseno==e:
    if i%2!=0:
        soma_cosseno=soma_cosseno+(((pi/5)**j)/fatorial(j))
    else:
        soma_cosseno=soma_cosseno-(((pi/5)**j)/fatorial(j))
    j=j+2
    i=i+1
    
cosseno=1-soma_cosseno

#DOUBLE CALCULA_RAZAO_AUREA_:
razaoAurea= 2*cosseno
print('%.15f' %pi)
print('%.15f' %razaoAurea)