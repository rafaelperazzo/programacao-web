# -*- coding: utf-8 -*-
from __future__ import division 

def contido(lista1,lista2):
    contador=0
    for i in range(0,len(lista2),1):
        if lista2[i] in lista1:
            contador=contador+1
    return contador
    

n=input('digite a quantidade de elementos de a:')
m=input('digite a quantidade de elementos de b:')

a=[]
for i in range(0,n,1):
    a.append(input('digite um elemento:'))

b=[]
for i in range(0,n,1):
    b.append(input('digite um elemento:'))
    
print contido(a,b)
