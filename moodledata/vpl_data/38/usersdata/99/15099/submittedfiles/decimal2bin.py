# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite um número de base binária:'))

a=n
contador=0
i=0
while i<a:
    a=a//10
    contador=contador+1

b=n    
soma=0    
while i<n:
    x=b%10
    b=b//10
    soma=soma+(x*(2**i))
    i=i+1
print soma
    