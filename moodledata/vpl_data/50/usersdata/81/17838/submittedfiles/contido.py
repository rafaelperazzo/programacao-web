# -*- coding: utf-8 -*-
from __future__ import division


def cont(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] in b:
            cont=cont+1
    return cont


n=input('Digite a quantidade de elementos de a:')
m=input('Digite a quantidade de elementod de b:')
a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Digite um valor de a:'))
for i in range(0,m,1):
    b.append(input('Digite um valor de b:'))

print cont(a,b)