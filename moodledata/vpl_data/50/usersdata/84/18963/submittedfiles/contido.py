# -*- coding: utf-8 -*-
from __future__ import division

def contido(c,d):
    contador=0
    for i in range (0,len(d),1):
        if d[i] in c:
            contador=contador+1
            
    return contador
    
n=input('digite a quantidade de elementos da lista:')
m=input('digite a quantidade de elementos da lista:')
a=[]
b=[]

for i in range(0,n,1):
    a.append(input('digite o valor:'))
for i in range(0,m,1):
    b.append(input('digite o valor:'))
    
print contido (a,b)