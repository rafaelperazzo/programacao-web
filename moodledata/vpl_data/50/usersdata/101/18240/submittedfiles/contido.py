# -*- coding: utf-8 -*-
from __future__ import division

def contido (a,b):
    cont = 0
    for i in range (0,len(b), 1):
        if b[i] in a:
            cont = cont + 1
            
    return cont

a = []
b = []

n = input(' Digite a quantidade de elementos em a: ')
m = input(' Digite a quantidade de elementos em b: ')


for i in range (0, n, 1):
    a.append(input('Digite um elemento de a: '))

for i in range (0, m, 1):
    b.append(input('Digite um elemento de b: '))
    

print contido(a,b)
    