# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range (0,(len(lista)-2),1):
        if lista[i]<lista[i+1]:
        else:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False        
    #escreva o código da função crescente aqui


#escreva as demais funções

def decrescente(lista):
    cont=0
    for i in range(0,(len(lista)-2),1):
        cont=0
        for i in range(0,(len(lista)-2),1):
            if lista[i]>lista[i+1]:
            else:
                cont=cont+1
        if cont==0:
            return True
        else:
            return False

def consecutivos(lista):
    cont=0
    for i in range (0,(len(lista)-2),1):
        if lista[i]!=lista[i+1]:
        else:
            cont=cont+1
    if cont==0:
        return True
    else
        return False

#escreva o programa principal
n=input('Digite um valor n')
a=[]
b=[]
c=[]

for i in range(0,n,1):
    a.append(input('Digite um valor:'))

for i in range(0,n,1):
    b.append(input('Digite um valor:'))

for i in range(0,n,1):
    c.append(input('Digite um valor:'))

if crescente(a):
    print 'S'
else:
    print 'N'

if decrescente(a):
    print 'S'
else:
    print 'N'
    
if consecutivos(a):
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
    
if consecutivos(b):
    print 'S'
else:
    print 'N'


if crescente(c):
    print 'S'
else:
    print 'N'

if decrescente(c):
    print 'S'
else:
    print 'N'
    
if consecutivos(c):
    print 'S'
else:
    print 'N'