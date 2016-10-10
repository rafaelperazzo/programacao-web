# -*- coding: utf-8 -*-
from __future__ import division
import math
 
n=input('Digite o valor de n:')
soma = 0
j = 1
for i in range (1,n,1):
    if n%2==0:
        soma=soma + 1/j
    
else: 
    soma=soma - (1/j) 
    j = j + 1 
    
    
print('soma=%f.5:'%soma)

