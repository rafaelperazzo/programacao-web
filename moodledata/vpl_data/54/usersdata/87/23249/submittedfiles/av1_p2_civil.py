# -*- coding: utf-8 -*-
from __future__ import division

def modulo(lista):
    if lista<0:
        lista=lista*(-1)
        return lista
    else:
        return lista

def maior(lista):
    j=lista[0]
    for i in range (0,len(lista),1):
        if lista[i]>j:
            j=lista[i]
    return j
        
    
def menor(lista):
    j=lista[0]
    for i in range (0,len(lista),1):
        if lista[i]<j:
            j=lista[i]
    return j
    

def soma(lista,lista1):
    altura=modulo(maior(lista)-lista1)-modulo(menor(lista)-lista1)
    return altura
    


n=input('valor de n:')
m=input('valor de m:')
h=[]
for i in range(0,n,1):
    h.append(input('digite alturas:'))

print('%d' %(soma(h,m)))