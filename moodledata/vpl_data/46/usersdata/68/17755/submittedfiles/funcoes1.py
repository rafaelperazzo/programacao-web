# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range (0, len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
if cont==0:
    return True
else:
    return False

def decrescente(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
if cont==0:
    return True
else:
    return False

def elementos_iguais(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
if cont==0:
    return True
else:
    return False
    
#programa principal
n=input('Digite n:')
a=[]
b=[]
c=[]
for i in range (0,n,1):
    a.append (input('Digite um elemento da lista a:'))
for i in range (0,n,1):
    b.append (input('Digite um elemento da lista b:'))
for i in range (0,n,1):
    c.append (input('Digite um elemento da lista c:'))
    
if crescente(a):
    print ('S')
else:
    print ('N')

if decrescente(a):
    print ('S')
else:
    print ('N')

if elementos_iguais(a):
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

if elementos_iguais(b):
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

if elementos_iguais(c):
    print ('S')
else: 
    print ('N')