# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    if i==0:
        if lista[i]>lista[i+1]:
            cont=cont+1
    elif lista[i]>lista[i+1] and lista[i]>lista[i-1]:
        cont=cont+1
    elif i==len(lista)-1:
        if lista[len(lista)-1]>lista[(len(lista)-2]:
            con=cont+1
    if cont==1:
        return True
    else:
        return False

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
    
    
    
    
    
