# -*- coding: utf-8 -*-
from __future__ import division
import math

m=input('Digite a quantidade de termos:')

soma=0

i=0
j=2

while i<m:
    if i%2==0:
        soma=soma+(4/(j*(j+1)*(j+2)))
        
    else:
        soma=soma-(4/(j*(j+1)*(j+2)))
    
    i=i+1   
    j=j+2
    soma=3+soma
    
print(soma)

