# -*- coding: utf-8 -*-
from __future__ import division


b=input('Digite a base binária:')

k=b

contador=0

while k>0:
    k=k//10
    contador=contador+1
    
n=contador
i=0
soma=0

while i<=(n-1):
    r=b%10
    b=b//10
    d=r*(2**i)
    soma=soma+d
    i=i+1
print(soma)