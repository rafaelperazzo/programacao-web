# -*- coding: utf-8 -*-
from __future__ import division

d=input('Digite o valor natural na base decimal:')

k=d
contador=0

while k>0:
    k=k//2
    contador=contador+1
    
n=contador
i=0
soma=0
r=d

while i<=(n-1):
    r=d%2
    d=d//2
    b=r*(10**1)
    i=i+1
    soma=soma+b
    
print(soma)