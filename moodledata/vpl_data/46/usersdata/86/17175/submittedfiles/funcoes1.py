# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+0
        else:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
def decrescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+0
        else:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
def consecutivos(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont==1:
        return True
    else:
        return False
n=input('n:')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(input())
for j in range(0,n,1):
    b.append(input())
for k in range(0,n,1):
    c.append(input())
if crescente(a)==True:
    print('S')
else:
    print('N')
if crescente(b)==True:
    print('S')
else:
    print('N')
if crescente(c)==True:
    print('S')
else:
    print('N')
if decrescente(a)==True:
    print('S')
else:
    print('N')
if decrescente(b)==True:
    print('S')
else:
    print('N')
if decrescente(c)==True:
    print('S')
else:
    print('N')
if consecutivos(a)==True:
    print('S')
else:
    print('N')
if consecutivos(b)==True:
    print('S')
else:
    print('N')
if consecutivos(c)==True:
    print('S')
else:
    print('N')
    

    

