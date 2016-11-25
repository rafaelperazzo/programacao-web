# -*- coding: utf-8 -*-
from __future__ import division

def maior(lista):
    cont = 0
    for i in range (0, len(lista), 1):
        if lista[i] > lista[i+1] or lista[i] < lista[i+1]:
            x = lista[i] - lista[i+1]
            cont = cont + 1
        if x > len(lista):
            return x
            
a = []
n = input('Digite o número de termos da lista: ')
for i in range (0,n,1):
    a.append(input('Digite um termo: '))

print (maior(a))