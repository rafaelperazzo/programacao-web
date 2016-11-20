# -*- coding: utf-8 -*-
from __future__ import division
def crescente(lista):
    cont =0
    for i in range(0,len(lista)-1,1):
        if lista[i]>=lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
def decrescente(lista):
    cont = 0
    for i in range (0,len(lista)-1,1):
        if list[i]<=lista[i+1]:
            cont = cont +1
    if cont ==0:
        return True
    else:
        return False
def igual(lista):
    cont =0
    for i in range(0, len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont =cont +1
    if cont!=0:
        return True
    else:
        return False
n = input ('N:')
a=[]
b=[]
c=[]
for j in range (0,n,1):
    a.append(input('elementos:'))
for k in range (0,n,1):
    b.append(input('elementos:'))
for l in range (0,n,1):
    c.append(input('elementos:'))
if crescente(a):
    print 'S'
else:
    print 'N'
if decrescente(a):
    print 'S'
else:
    print 'N'
if igual(a):
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
if igual(b):
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
if igual(c):
    print 'S'
else:
    print 'N'