# -*- coding: utf-8 -*-
from __future__ import division

d=input('valor do número natural na base decimal:')
k=d
cont=0
while k>0:
    k=k//2
    cont=cont+1
n=cont
i=0
soma=0
r=d
while i<=(n-1):
    r=d%2
    d=d//2
    b=r*(10**i)
    i=i+1
    soma=soma+b
print soma
