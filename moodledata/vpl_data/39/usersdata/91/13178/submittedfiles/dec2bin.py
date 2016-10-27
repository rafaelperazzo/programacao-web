# -*- coding: utf-8 -*-
from __future__ import division

d=input('digite um numero natural de base decimal:')
cont=0
x=d
while x>0:
    x=x//2
    cont+=1
n=cont
i=0
soma=0
y=d
while i<=(n-1):
    y=d%2
    d=d//2
    b=r*(10**i)
    i+=1
    soma=soma+b
print soma