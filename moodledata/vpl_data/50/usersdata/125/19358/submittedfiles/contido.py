# -*- coding: utf-8 -*-
from __future__ import division

def contido(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] in b:
            cont = cont+1
    return cont

n=input('Digite a quantidade de elementos em a:')
m=input('Digite a quantidade de elementos em b:')

a=[]
b=[]
for i in range(0,n,1):
    a.append(input('Digite um valor para a lista a:'))

for i in range(0,m,1):
    b.append(input('Digite um valor um valor para a lista b:'))
    
print contido(a,b)