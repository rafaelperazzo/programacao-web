# -*- coding: utf-8 -*-
from __future__ import division

def maiorDegrau(l):
    
    maiorD=0
    for i in range(0,(len(l)-1),1):
        degrau=l[i]-l[i+1]
        if degrau<0:
            degrau=degrau*(-1)
        
        if degrau>maiorD:
            maiorD=degrau
        
        
    return maiorD

n=input('Quantidade de termos: ')
lista=[]

for i in range (0,n,1):
    lista.append(input('Digite um termo: '))

print maiorDegrau(lista)