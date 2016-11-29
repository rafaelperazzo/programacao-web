# -*- coding: utf-8 -*-
from __future__ import division
import math
def modulo(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        x=x*(1)
        return x
    
def maiorDegrau(lista):
    maior=0
    for i in range(0,len(lista)-1,1):
        degrau=int(math.fabs(lista[i]-lista[i+1])) #Faltou o int aqui!!
        if degrau>maior:
            maior=degrau
            
    return maior

n=input('dgite a quantidade de elementos da lista:')

lista=[]
for i in range(0,n,1):
    lista.append(input('digite um elemento da lista:'))
    
print(maiorDegrau(lista))