# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont = 0
    for i in range(0,len(lista),1):
        if lista[i] >= lista[i+1]:
            cont = cont +1
    if cont == 0:
        return S
    else:
        return N

def decrescente(lista):
    cont = 0
    for i in range(0,len(lista),1):
        if lista[i] <= lista[i+1]:
            cont = cont +1
    if cont == 0:
        return S
    else:
        return N

def consecutivos(lista):
    cont = 0
    for i in range(0,len(lista),1):
        if lista[i] == lista[i+1]:
            cont = cont +1
    if cont != 0:
        return S
    else:
        return N
        

n = input('Digite a quantidade de termos da lista:')
a = []
b = []
c = []

for i in range(0,n,1):
    a.append(input('Digite um valor para a lista 1:'))

for i in range(0,n,1):
    b.append(input('Digite um valor para a lista 2:'))    

for i in range(0,n,1):
    c.append(input('Digite um valor para a lista 3:'))

print(crescente(a))
print(decrescente(a))
print(consecutivos(a))
print(crescente(b))
print(decrescente(b))
print(consecutivos(b))
print(crescente(c))
print(decrescente(c))
print(consecutivos(c))




