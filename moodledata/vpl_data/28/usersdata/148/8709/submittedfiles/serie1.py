# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n = input('Digite o valor de n:')
soma = 0
#PROCESSAMENTO
for i in range (1,n+1,1):
    b = i/(i*i)
    if i%2==0:
        soma=soma-b
    else :
        soma=soma+b
print ('%.5f' %soma)
