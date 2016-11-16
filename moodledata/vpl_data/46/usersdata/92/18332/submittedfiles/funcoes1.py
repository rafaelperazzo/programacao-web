# -*- coding: utf-8 -*-
from __future__ import division

def crescente (x):
    cont=0
    for i in range(0, len(x)-1, 1):
        if x[i]>x[i+1]:
            cont= cont+1
            break
    if cont==0:
        return "S"
    else:
        return "N"

def decrescente (x):
    cont=0
    for i in range(0, len(x)-1, 1):
        if x[i]<x[i+1]:
            cont= cont+1
            break
    if cont==0:
        return "S"
    else:
        return "N"

def iguais (x):
    cont=1
    for i in range(0, len(x)-1, 1):
        if x[i]==x[i+1]:
            cont= cont-1
            break
    if cont==0:
        return "S"
    else:
        return "N"

n= input('Digite n: ')
a=[]
for i in range(0, n, 1):
    a.append(input( ))
b=[]
for i in range(0, n, 1):
    b.append(input( ))
c=[]
for i in range(0, n, 1):
    c.append(input( ))

print crescente(a)
print decrescente(a)
print iguais(a)
print crescente(b)
print decrescente(b)
print iguais(b)
print crescente(c)
print decrescente(c)
print iguais(c)



