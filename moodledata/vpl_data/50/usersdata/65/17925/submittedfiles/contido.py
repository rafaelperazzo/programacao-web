# -*- coding: utf-8 -*-
from __future__ import division

def Econtidos(lista1,lista2):
    contador=0
    for i in range(0,len(lista1),1):
        if a[i] in b:
            contador=contador+1
    
    return contador

na=input('Digite a quantidade de elementos de a: ')
nb=input('Digite a quantidade de elementos de b: ')
a=[]
b=[]

for i in range(0,na,1):
    a.append(input('Digite os elementos de a: '))

for i in range(0,nb,1):
    b.append(input('Digite os elementos de b: '))

print(Econtidos(a,b))
