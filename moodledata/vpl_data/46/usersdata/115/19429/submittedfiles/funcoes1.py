# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    c=0
    for i in range(0,len(lista)-1,1):
        if (lista[i]>lista[i+1]):
            c=c+1
        if c==0:
            return true
        else:
            return false
def decrescente(lista):
    c=0
    for i in range (0,len(lista)-1,1):
        if (lista[i]<lista[i+1]):
            c=c+1
        if c==0:
            return true
        else:
            return false
def igual(lista):
    c=0
    for i in range(0,len(lista)-1,1):
        if (lista[i]==lista[i+1]):
            c=c+1
        if c!=0:
            return true
        else:
            return false
def inserir_lista(lista,n):
    for i in range(0,n,1):
        lista.append(input('insira o elemento:'))
    return lista

n=int(input('quantidade de elementos da lista:'))
x=[]
y=[]
z=[]
print('insira a primeira lista:')
x = inserir_lista(x,n)
print('insira a segunda lista:')
y = inserir_lista(y,n)
print('insira a terceira lista:')
z = inserir_lista(z,n)

if crescente(x):
    print('S')
    print('N')
    print('N')
else:
    print('N')
    if decrescente(x):
        print('S')
        print('N')
    else:
        print('N')
        if igual(x):
            print('S')
        else:
            print('N'')
if crescente(y):
    print('S')
    print('N')
    print('N')
else:
    print('N')
    if decrescente(y):
        print('S')
        print('N')
    else:
        print('N')
        if igual(y):
            print ('S')
        else:
            print('N')
if crescente(z):
    print('S')
    print('N')
    print('N')
else:
    print('N')
    if decrescente(z):
        print('S')
        print('N')
    else:
        print('N')
        if igual(z):
            print('S')
        else:
            print('N')


            