# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=input('Digite o valor do primeiro número:')
b=input('Digite o valor do segundo número:')
#PROCESSAMENTO+SAÍDA
i=1
while i>0:
    if a%i==0 and b%i==0 and i!=1:
        print(i)
        break
    elif i==1:
        print (i)
        break
    else:
        i=i+1

