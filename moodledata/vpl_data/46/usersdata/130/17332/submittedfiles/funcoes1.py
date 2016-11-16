# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
def decrescente (lista):
    cont=0
    i=len(lista)-1
    while i>=0:
        if lista[i]>lista[i-1]:
            cont=cont+1
        i=i-1    
    if cont==len(lista)-1:
        return True
    else:
        return False
    
def C.iguais (lista):
    for i in range(0,len(lista),1):
        if lista[i]==lista[i+1]:
            return True
        else:
            return False
a=[]
b=[]
c=[]
n=input('Digite o valor de n:')
for i in range(0,n,1):
    a.append(input('Digite um elemento:')
for i in range(0,n,1):
    b.append(input('Digite um elemento:')
for i in range(0,n,1):
    c.append(input('Digite um elemento:')
if crescente(a):
    print('S')
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')
if C.iguais(a):
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
if C.iguais(b):
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
if C.iguais(c):
    print('S')
else:
    print('N')




#escreva o programa principal
