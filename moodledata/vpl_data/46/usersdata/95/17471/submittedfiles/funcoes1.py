# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont+=1
    if cont==0:
        return True
    else:
        return False
def decrescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont+=1
    if cont==0:
        return True
    else:
        return False
def consecutivosiguais(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False


#escreva o programa principal
n=input('Quantidade de elementos da lista:')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(input('Valor de a:'))
    
for i in range(0,n,1):
    b.append(input('Valor de b:'))
    
for i in range(0,n,1):
    c.append(input('Valor de c:'))

if crescente(a):
    print ('S')
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')
if consecutivosiguais(a):
    print ('S')
else:
    print('N')

if crescente(b):
    print ('S')
else:
    print('N')
if decrescente(b):
    print('S')
else:
    print('N')
if consecutivosiguais(b):
    print ('S')
else:
    print('N')
    
if crescente(c):
    print ('S')
else:
    print('N')
if decrescente(c):
    print('S')
else:
    print('N')
if consecutivosiguais(c):
    print ('S')
else:
    print('N')