# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1] and lista[i]>lista[i-1]:
            break
    



n = input('Digite a quantidade de elementos da lista: ')
a=[]

for i in range(0,n,1):
    a.append(input('Digite um valor de a:'))
    
print pico(a)
    
