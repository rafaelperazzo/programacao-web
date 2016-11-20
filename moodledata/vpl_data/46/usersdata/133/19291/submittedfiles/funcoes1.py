# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
c = 0
for i in range(0, len(lista) - 1, 1):
    if (lista[i] > lista[i+1]):
        c = c + 1
if c == 0:
    return True
else:
    return False


def decrescente (lista):
c = 0
for i in range (0, len(lista) - 1, 1):
    if(lista[i] < lista[i+1]):
        c = c + 1
if c == 0:
    return True
else:
    return False
    
def iguais(lista):
c = 0
for i in range(0, len(lista) - 1, 1):
    if(lista[i] == lista[i+1]):
        c = c + 1
if c!=0:
    return True
else:
    return False
    
def insere_lista(lista):
for i in range(0, len(lista), 1):
    lista.append(input('Digite o elemento:'))
return lista


n = int(input('Digite o número de elementos da lista:'))
a = [], b = [], c = []
print('Preencha a lista 1:')
a = insere_lista(a)
print('Preencha a lista 2:')
b = insere_lista(b):
print('Preencha a lista 3:')
c = insere_lista(c)

if crescente(a):
    print('S')
else:
    print('N')