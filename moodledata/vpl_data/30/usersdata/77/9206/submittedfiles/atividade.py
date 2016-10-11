# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))
soma=0
i=1
j=1
k=0

while i>=n:
    if n>0:
        soma=soma+(j/n-k)
        
    elif n<0:
        n*(-1)
        
        soma=soma+(j/n-k)
        
print(soma)
