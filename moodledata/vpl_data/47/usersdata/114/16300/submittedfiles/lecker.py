# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        if i==len(lista-1):
            if lista[len(lista)-1]>lista[len(lista)-2]:
                cont=cont+1
        else:
            if lista[i-1]<lista[i]>lista[i+1]:
                cont=cont+1
    if cont=1            
        return true
    else:
        return false
n=input('digite o valor de n: ')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('digite os n valores da lista a : '))
for i in range(0,n,1):
    b.append(input('digite os n valores da lista b : '))

if lecker(a):
    print('S')
else:
    print('N')
if lecker(b):
    print('S')
else:
    print('N')    
    
