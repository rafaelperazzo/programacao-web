# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    a = 0
    for i in range (0, len(lista)-1, 1):
        if lista[i] < lista[i+1]:
            a = a + 1
    if a == len(lista) - 1:
        return True
    else:
        return False
   
def decrescente (lista):
    b = 0
    for i in range (0, len(lista)-1, 1):
        if lista[i] > lista[i+1]:
            b = b + 1
    if b == len(lista) - 1:
        return True
    else:
        return False

def eci(lista):
    c = 0
    for i in range (0, len(lista)-1, 1):
        if lista[i] == lista[i+1]:
            c = c + 1
    if c > 0:
        return True
    else:
        return False

n = input('Digite o número de elementos das listas: ')
l1 = []
l2 = []
l3 = []
for i in range (0, n, 1):
    l1.append(input('Digite um valor para a lista 1: '))
for i in range (0, n, 1):
    l2.append(input('Digite um valor para a lista 2: '))
for i in range (0, n, 1):
    l3.append(input('Digite um valor para a lista 3: '))
if crescente(l1):
    print('S')
else:
    print('N')
if decrescente(l1):
    print('S')
else:
    print('N')
if eci(l1):
    print('S')
else:
    print('N')
if crescente(l2):
    print('S')
else:
    print('N')
if decrescente(l2):
    print('S')
else:
    print('N')
if eci(l2):
    print('S')
else:
    print('N')
if crescente(l3):
    print('S')
else:
    print('N')
if decrescente(l3):
    print('S')
else:
    print('N')
if eci(l3):
    print('S')
else:
    print('N')