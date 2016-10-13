# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o valor de n: ')
soma=0
i=1

while True:
    valor=n/i
    soma=valor+soma
    n=n-1
    i=i+1
    
print('%.5f'%soma)