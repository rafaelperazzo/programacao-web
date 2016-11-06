# -*- coding: utf-8 -*-
from __future__ import division

b=input('digite um número natural na base binária:')
k=b
cont=0
while k>0:
    k=k//10
    cont+=1

n=cont
i=0
soma=0
while i<=(n-1):
    r=d%10
    d=d//10
    h=r*(2**i)
    i=i+1
    soma=soma+h
print soma




