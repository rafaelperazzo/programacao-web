# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    j=0
    for i in range(0,len(lista),1):
        if lista[i]<lista[i+1]:
            j=j+1
            c=True
    for i in range(j,len(lista),1):
        if lista[i]>lista[i+1]:
            j=j+1
            d=True
    if c and d and j==len(lista):
        return True
    else:
        return False
        
n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
for i in range(0,n,1):
    a.append(input('a:'))

if pico(a):
    print ('S')
else:
    print('N')