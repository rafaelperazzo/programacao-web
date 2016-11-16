# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
        else:
            cont=1
    if cont==0:
        return ('S')
    else:
        return ('N')
def decresente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
        else:
            cont=1
    if cont==0:
        return ('S')
    else:
        return ('N')
def consecutivos(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]=lista[i+1]:
        cont=1
    if cont==0:
        return ('S')
    else:
        return ('N')
n=input('n:')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(input('digite a:'))
for i in range(0,n,1):
    b.append(input('digite b:'))
for i in range(0,n,1):
    c.append(input('digite c:'))
print crescente(a)
print crescente(b)    
print crescente(c)
print decrescente(a)
print decrescente(b)
print decrescente(c)
print consecutivos(a)
print consecutivos(b)
print consecutivos(c)
