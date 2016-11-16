# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def dec(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def iguais(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont>0:
        return True
    else:
        return False
        

#escreva o programa principal

n=input('digite a quantidade de elementos:')
a=[]
b=[]
c=[]

for i in range(0,n,1):
    a.append(input('Digite um elemento para A:'))

for i in range(0,n,1):
    b.append(input('Digite um elemento para B:'))

for i in range(0,n,1):
    c.append(input('Digite um elemento para C:'))


#chamando funções
if crescente(a):
    print('S')
else:
    print('N')

if dec(a):
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

if dec(b):
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

if dec(c):
    print('S')
else:
    print('N')

if iguais(c):
    print('S')
else:
    print('N')