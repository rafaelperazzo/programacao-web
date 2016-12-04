# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

m=int(input('digite o valor de m:'))
e=input('digite o valor de epsilon:')

m=funcoes.absoluto(m)
pi=funcoes.calculopi(m)
cosseno=funcoes.calculocosseno(pi/5,e)
print cosseno
razaoaurea=funcoes.calculorazaoaurea(m,e)

print('%.15f' %pi)
print('%.15f' %razaoaurea)
        
        
