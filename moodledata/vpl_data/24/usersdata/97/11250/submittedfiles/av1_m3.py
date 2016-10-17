# -*- coding: utf-8 -*-
from __future__ import division
import math

m=input('digite o valor de m:')
h=2
i=3
j=4
soma=0
cont=0
while i<=m:
    if cont%2==0:
        soma=soma - 4/(h*i*j)
    else:
        soma=soma + 4/(h*i*j)
    
    h=h+2
    i=i+2
    j=j+2
soma=soma+3
print('%.6f'%soma)
