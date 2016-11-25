# -*- coding: utf-8 -*-
from __future__ import division
def degrau(z):
    maior=0
    for i in range(0,len(z)-1,1):
        j=z[i+1]-z[i]
        if j<0:
            j=j*(-1)
        if j>maior:
            maior=j
    return maior

n=input('Digite a quantidade de elementos da lista:')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento:'))

deg=degrau(a)    
print(deg)



    
