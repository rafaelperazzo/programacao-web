# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite um numero:'))

a=n
contador=contador+1
i=0

while i<a:
    a=a//2
    contador=contador+1
    
b=n
soma=0
while i<n:
    x=b%2
    b=b//2
    soma=soma+(x*(10**i))
    i=i+1
print soma
    
