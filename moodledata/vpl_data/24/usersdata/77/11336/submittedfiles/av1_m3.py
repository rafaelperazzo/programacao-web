# -*- coding: utf-8 -*-
from __future__ import division
import math

m=input('Digite a quantidade de termos:')

soma=0

j=2

for i in range(1,m,1):
    if i%2==0:
        soma=soma+(4//(j*(j+1)*(j+2)))
        
    else:
        soma=soma-(4//(j*(j+1)*(j+2)))
        
    j=j+2
    soma=soma+3
    
print(soma)

