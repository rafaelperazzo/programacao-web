# -*- coding: utf-8 -*-
from __future__ import division

def incluso(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] in b:
            cont = cont +1
    if cont!=0:
        return True
    else:
        return False
    

n=input('Tamanho da lista : ')
a=[]
for i in range(0,n,1):
    a.append(input('Elementos da lista1: '))

n2=input('Tamanho da lista : ')
b=[]
for i in range(0,n2,1):
    b.append(input('Elementos da lista2: ')

if incluso(a,b)
    