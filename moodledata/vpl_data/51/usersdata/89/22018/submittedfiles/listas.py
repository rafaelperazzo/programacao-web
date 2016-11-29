# -*- coding: utf-8 -*-
from __future__ import division

def modulo(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        x=x*(1)
        return x
    
def maiorDegrau(a):
    maior=0
    for i in range(0,len(a)-1,1):
        degrau=(a[i]-a[i+1])
        if degrau>maior:
            maior=degrau
            
    return maior

n=input('dgite a quantidade de elementos da lista:')

lista=[]
for i in range(0,n,1):
    lista.append(input('digite um elemento da lista:'))
    
print(maiorDegrau(lista))