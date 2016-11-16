# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    for i in range(0,len(lista),1):
        if x[i]<x[i+1]:
            return True
        else:
            return False

#escreva as demais funções
def decrescente (lista):
    for i in range(0,len(lista),1):
        if x[i]>x[i+1]:
            return True
        else:
            return False

def iguais (lista):
    for i in range(0,len(lista),1):
        if x[i]==x[i+1]:
            return True
        else:
            return False

#escreva o programa principal
n=input('digite o número de elementos:')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(input('digite um elemento:'))
for i in range(0,n,1):
    b.append(input('digite um elemento:'))
for i in range(0,n,1):
    c.append(input('digite um elemento:'))

if crescente(a):
    print('S')
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')
if iguais(a):
    print('S')
else:
    print('N')
if crescente(b):
    print('S')
else:
    print('N')
if decrescente(b):
    print('S')
else:
    print('N')
if iguais(b):
    print('S')
else:
    print('N')
if crescente(c):
    print('S')
else:
    print('N')
if decrescente(c):
    print('S')
else:
    print('N')
if iguais(c):
    print('S')
else:
    print('N')




