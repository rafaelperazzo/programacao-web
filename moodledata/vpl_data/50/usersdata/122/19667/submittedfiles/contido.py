# -*- coding: utf-8 -*-
from __future__ import division

def contido (a,b):
    cont=0
    for i in range (0,len(a),1):
        if a[i] in b:
            cont=cont+1
    return cont
    
n=input('Digite o número de elementos de a:')
m=input('Digite o número de elementos de b:')
a=[]
b=[]

for i in range (0,n,1):
    a.append(input('Digite um valor'))
    
for i in range (0,m,1):
    b.append(input('Digite um valor'))

print contido (a,b)