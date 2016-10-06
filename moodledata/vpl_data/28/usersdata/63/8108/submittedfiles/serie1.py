# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de termos:')
soma=0
i=1
j=(i)**2

while i>=n:
    if i%2==0:
        soma=soma-i/j
    else:
        soma=soma+i/j
    
    i=i+1
    
    
    
    print('%.5f '%soma)