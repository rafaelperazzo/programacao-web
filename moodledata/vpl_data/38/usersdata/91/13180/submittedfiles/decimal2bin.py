# -*- coding: utf-8 -*-
from __future__ import division

b=input('digite um numero natural na base binaria:')
x=b
cont=0
while x>0:
    x=x//10
    cont+=1
n=cont
i=0
soma=0
while i<=(n-1):
    y=b%10
    b=b//10
    d=y*(2**i)
    soma+=d
    i=i+1
print soma