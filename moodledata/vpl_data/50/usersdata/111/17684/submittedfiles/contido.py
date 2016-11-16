# -*- coding: utf-8 -*-
from __future__ import division

def incluso(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] in b:
            cont = cont +1
    return cont
    

n=input('Tamanho da lista1 : ')
p=input('Tamanho da lista2 : ')
a=[]
for i in range(0,n,1):
    a.append(input('Elementos da lista1: '))
b=[]
for i in range(0,p,1):
    b.append(input('Elementos da lista2: '))

c=incluso(a,b)
print c
    