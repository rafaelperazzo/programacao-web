# -*- coding: utf-8 -*-
from __future__ import division

n= input('Insira n:')
L=[]
for x in range (0,n,1):
    L.append(input('Insira um valor:'))
somaI=0
somaP=0
contI=0
contP=0
for i in range (0,len(x),1):
    if (L[i] % 2)==0:
        somaP= somaP + L[i]
        contP= contP + 1
    elif (L[i] % 2)!=0:
        somaI= somaI + L[i]
        contI= contI + 1
print (somaI)
print (somaP)
print (contI)
print (contP)
print (L)