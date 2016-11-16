# -*- coding: utf-8 -*-
from __future__ import division
def qiguais(a,b):
    cont=0
    for i in range(0, len(a),1):
        for j in range(0, len(b),1):
            if a[i]==b[j]:
                cont=cont+1
    return cont
n=input('numero de elementos da lista 1: ')
m=input('numero de elementos da lista 2: ')
a=[]
b=[]
for i in range(0, n,1):
    a.append(input('elemento de a: '))
for j in range(0, m,1):
    b.append(input('elemento de b: '))
print(qiguais(a,b))