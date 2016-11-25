# -*- coding: utf-8 -*-
from __future__ import division

def modulo(t):
    mod= ((t**2)**0.5)
    return mod
    
def variacao(t,lista):
    posicao=0
    for i in range(0,len(lista)-1,1):
        mod(lista[i+1]-lista[i])
        posicao=i
    return variacao
        
a=[]
n=input('Digite a quantidade de n')

for i in range(0,n,1):
    a.append(input('Digite um elemento de a:'))
    
resultado=variacao(t,a)
print resultado