# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==len(lista):
        return True
    else:
        return False

#escreva as demais funções
def decrescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==len(lista):
        return True
    else:
        return False

def iguais (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont>0:
        return True
    else:
        return False

#escreva o programa principal
a=[]
b=[]
c=[]
n=input('digite o número de elementos:')
for i in range(0,n,1):
    a.append(input('digite um elemento:'))
for i in range(0,n,1):
    b.append(input('digite um elemento:'))
for i in range(0,n,1):
    c.append(input('digite um elemento:'))

if crescente(a):
    print ('S')
else:
    print ('N')
if decrescente(a):
    print ('S')
else:
    print ('N')
if iguais(a):
    print ('S')
else:
    print ('N')
if crescente(b):
    print ('S')
else:
    print ('N')
if decrescente(b):
    print ('S')
else:
    print ('N')
if iguais(b):
    print ('S')
else:
    print ('N')
if crescente(c):
    print ('S')
else:
    print ('N')
if decrescente(c):
    print ('S')
else:
    print ('N')
if iguais(c):
    print ('S')
else:
    print ('N')




