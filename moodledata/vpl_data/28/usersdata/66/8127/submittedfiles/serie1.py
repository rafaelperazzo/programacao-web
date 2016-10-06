# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=input('Digite o valor de n: ')
soma=0

#PROCESSAMENTO
for i in range (1,n+1,1):
    if i%2==0:
        soma=soma-(i/(i**2))
    else:
        soma=soma+(i/(i**2))
    
#SAIDA
print soma 