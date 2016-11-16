# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
def decrescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
    
def iguais (lista):
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
    a.append(input('Digite um elemento:'))
for i in range(0,n,1):
    b.append(input('Digite um elemento:'))
for i in range(0,n,1):
    c.append(input('Digite um elemento:'))
if crescente(a)==True:
    print('S')
else:
    print('N')
if decrescente(a)==True:
    print('S')
else:
    print('N')
if iguais(a)==True:
    print('S')
else:
    print('N')

if crescente(b)==True:
    print('S')
else:
    print('N')
if decrescente(b)==True:
    print('S')
else:
    print('N')
if iguais(b)==True:
    print('S')
else:
    print('N')

if crescente(c)==True:
    print('S')
else:
    print('N')
if decrescente(c)==True:
    print('S')
else:
    print('N')
if iguais(c)==True:
    print('S')
else:
    print('N')




#escreva o programa principal
