# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
m=input('digite o valor de m:')
i=2
soma=3
j=1

#PROCESSAMENTO
while j<=m:
    if i%4==0:
        soma=soma-(4/(i*(i+1)*(i+2)))
    else:
        soma=soma+(4/(i*(i+1)*(i+2)))
    i=i+2
    j=j+1
    
#SAIDA
print ('%.6f'% soma)

        
