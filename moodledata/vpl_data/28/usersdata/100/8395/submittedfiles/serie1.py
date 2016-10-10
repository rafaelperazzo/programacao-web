# -*- coding: utf-8 -*-
from __future__ import division
import math
n = input ('digite o valor de n:')
soma = 0
for i in range (1,n+1,1):
    b = i/(i**2)
    
    if b%2==0:
        soma = soma-b
    elif b!=0:
        soma = soma+b 
print ('%.5f'%soma)