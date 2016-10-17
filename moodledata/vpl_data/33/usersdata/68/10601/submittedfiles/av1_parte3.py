# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA:
n= input('Digite a quantidade de termos:')
i=0
j=1
soma=0

#PROCESSAMENTO:
while i<n:
    if i%2==0:
        soma=soma+(1/(j*(3**i)))
    else:
        soma=soma-(1/(j*(3**i)))
    j=j+2
    i=i+1
pi= (12**0.5)*soma

print ('%.6f' %pi)

