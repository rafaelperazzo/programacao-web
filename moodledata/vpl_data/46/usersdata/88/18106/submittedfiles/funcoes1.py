# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

def decrescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

def sequencia(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False

#escreva o programa principal
n=input('Digote a quantidade de elementos: ')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento de a: '))
for j in range(0,n,1):
    b.append(input('Digite um elemento de b: '))
for k in range(0,n,1):
    c.append(input('Digite um elemento de c: '))

if crescente(a):
    print 'S'
else:
    print 'N'
if decrescente(a):
    print 'S'
else:
    print 'N'
if sequencia(a):
    print 'S'
else:
    print 'N'

if crescente(b):
    print 'S'
else:
    print 'N'
if decrescente(b):
    print 'S'
else:
    print 'N'
if sequencia(b):
    print 'S'
    
if crescente(c):
    print 'S'
else:
    print 'N'
if decrescente(c):
    print 'S'
else:
    print 'N'
if sequencia(c):
    print 'S'
else:
    print 'N'