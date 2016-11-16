# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de elementos da lista:')
a=[]
for i in range (0,n,1):
    a.append(input('Digite o elemento da lista:'))
    
def pico(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1] and lista[i]>lista[i-1]:
            cont=cont+1
            if cont>0:
                return True
            else:
                return False
if pico(a):
    print(i)