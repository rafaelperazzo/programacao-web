# -*- coding: utf-8 -*-
from __future__ import division

def contido(a,b):
    for i in range(0,len(a),1):
        if a[i] in b:
            cont = cont + 1
    return cont

n=input('Digite a quantidade de elementos em a:')
m=input('Digite a quantidade de elementos em b:')

a=[]
for i in range(0,n,1):
    a.appende(input('Digite um valor:')
b=[]
for i in range(0,m,1):
    a.append(input('Digite um valor:')
    
print contido(a,b)