# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont+=1
    if cont==0:
        return True
    else:
        return False

def decrescente(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont+=1
    if cont==0:
        return True
    else:
        return False

def conseciguais(lista):
    cont=0
    for i in range (0, len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont+=1
    if cont!=0:
        return True
    else:
        return False
        
#escreva o programa principal
n=input('digite os valores:')
a=[]
b=[]
c=[]

for i in range(0,n,1):
    a.append(input('digite o valor:'))
for i in range(0,n,1):
    b.append(input('digite o valor:'))
for i in range(0,n,1):
    c.append(input('diite o valor:'))

if 
