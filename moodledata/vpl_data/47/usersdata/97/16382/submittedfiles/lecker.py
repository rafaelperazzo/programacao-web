# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    if lista[0]>lista[1]:
        cont=cont+1
    elif lista[i]>lista[i+1] and lista[i]>lista[i-1]:
        cont=cont+1
    elif len(lista)>len(lista-1):
        cont=cont+1
    return cont

l=[]
m=[]
n=input('digite o número de elementos:')
for i in range(0,n,1):
    l.append(input('digite um elemento:'))
for i in range(0,n,1):
    m.append(input('digite um elemento:'))

lecker_l=cont(l)
lecker_m=cont(m)

if cont(l)==1:
    print('S')
else:
    print('N')
if cont(m)==1:
    print('S')
else:
    print('N')
    
    
    
    
    
