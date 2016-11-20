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
    for i in range (0, len(lista)-1, 1):
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
    
def insere_lista(lista, n):
    for i in range(0, n, 1):
        lista.append(input('Digite o elemento:'))
    return lista


n = int(input('Digite o número de elementos da lista:'))
a = [], b = [], c = []
print('Preencha a lista 1:')
a = insere_lista(a, n)
print('Preencha a lista 2:')
b = insere_lista(b, n)
print('Preencha a lista 3:')
c = insere_lista(c, n)

if crescente(a):
    print('S')
    print('N')
    print('N')
else: 
    print('N')
    if decrescente(a):
        print ('S')
        print('N')
    else:
        print('N')
        if iguais(a):
            print('S')
        else:
            print('N')
            
if crescente(b):
    print('S')
    print('N')
    print('N')
else: 
    print('N')
    if decrescente(b):
        print ('S')
        print('N')
    else:
        print('N')
        if iguais(b):
            print('S')
        else:
            print('N')
            
if crescente(c):
    print('S')
    print('N')
    print('N')
else: 
    print('N')
    if decrescente(c):
        print ('S')
        print('N')
    else:
        print('N')
        if iguais(c):
            print('S')
        else:
            print('N')
        
    