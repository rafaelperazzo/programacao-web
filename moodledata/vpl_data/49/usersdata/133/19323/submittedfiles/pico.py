# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    p = 0
    for i in range(0, len(lista)-1, 1):
        if (lista[i]>lista[i+1]):
            p=i
            break
    c = 0
    for i in range(p, len(lista)-1, 1):
        if(lista[i] <= lista[i+1]):
            c = c + 1
    if c == 0 and p!= 0:
        return True
    else:
        return False
    
n = int(input('Digite o número de elementos da lista'))
a = []
for i in range(0, n, 1):
    a.append(input('Digite o elemento'))

if pico(a):
    print('S')
else:
    print('N')
    


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
