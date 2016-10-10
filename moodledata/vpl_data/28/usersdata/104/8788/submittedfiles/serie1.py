# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=input('Digite o valor de n:')
#SAÍDA+PROCESSAMENTO
soma=1
for i in range(2,n+1,1):
    if i%2==0:
        soma=soma-(1/i)
    else:
        soma=soma+(1/i)
print('%.5f'%(soma))
