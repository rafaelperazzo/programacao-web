# -*- coding: utf-8 -*-
from __future__ import division
d=input('digite um numero na base decimal:')
cont=0
k=d
while k>0:
    k=k//2
n=cont
i=0
soma=0
r=d
while i<=(n-1):
    r=d%2
    d=d//d
    b=r*(10**i)
    i+=1
    soma=soma+b
print soma    