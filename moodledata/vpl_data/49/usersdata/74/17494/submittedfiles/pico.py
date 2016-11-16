# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    i=1
    cont = 0
    while (len(lista)-1)>i:
        if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
            cont = cont+1
        i = i+1
    if cont>0:
        print('S')
    else:
        print('N')
    
n = input('Digite a quantidade de elementos da lista: ')

i = 1
a = []

while n>=i:
    a.append(input('Digite os numeros da lista: '))
    i = i+1
    
print(pico(a))