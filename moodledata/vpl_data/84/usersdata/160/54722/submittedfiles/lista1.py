# -*- coding: utf-8 -*-
from __future__ import division



    
def par(n):
    soma=0
    i=0
    while i<n:
        if n%2==0:
            soma=soma+i
        i=i+1
        return(soma)

def impar(n):
    soma=0
    i=0
    while i<n:
        if n%2==1:
            soma=soma+1
        i=i+1
        return(soma)
        
def quantpar(n):
    i=0
    cont=0
    while i<n:
        if i%2==0:
            cont=cont+1
        i=i+1
    return(cont)
    
def quantimpar(n):
    i=0
    cont=0
    while i<n:
        if i%2==1:
            cont=cont+1
        i=i+1
        return(cont) 
        
n=int(input('Digite a quantidade de elementos da lista:'))
a=[]
for i in range(1,n+1,1):
    valor=float(input('Digite a lista:'))
    a.append(valor)
    
print(par(a))
print(impar(a))
print(quantpar(a))
print(a)
print(quantimpar(a))
