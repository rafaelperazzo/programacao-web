# -*- coding: utf-8 -*-
from __future__ import division

def degrau(x):
    maior=0
    for i in range(0,len(x)-1,1):
        if degrau>maior:
            maior=degrau
    return maior
a=[]
n=input('digite os elementos de n:')
for i in range(0,n,1):
    a.append(input('digite o elemento:'))
    
valor=degrau(a)
print (valor)