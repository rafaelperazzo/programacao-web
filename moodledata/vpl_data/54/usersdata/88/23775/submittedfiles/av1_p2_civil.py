# -*- coding: utf-8 -*-
from __future__ import division
import math

def maior(lista):
    l=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]>l:
            l=lista[i]
    return l
    
def menor(lista):
    l=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]<l:
            l=lista[i]
    return l

def mov(lista,altura):
    soma=math.fabs(maior(lista)-altura)+math.fabs(menor(lista)-altura)
    return soma

n=int(input('Digite a quantidade de pinos: '))
m=int(input('Digite a altura: '))
a=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento: '))

movimentos=mov(a,m)

print ('%d' %movimentos)

    


