# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=int(input('Digite um numero:'))
soma=0
j=1

for i in range(1,n+1,1):
    if n%i==0:
        soma=soma+(1/(j*(3**i)))
    else:
        soma=soma-(1/(j*(3**i)))
    j=j+2
    soma=12**(1/2)*soma
print('%.6f'%soma)