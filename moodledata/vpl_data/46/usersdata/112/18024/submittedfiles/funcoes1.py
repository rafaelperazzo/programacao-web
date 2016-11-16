# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de números das listas:')
a=[]
b=[]
c=[]
for i in range (0,n,1):
    a.append(input('Digite um valor da lista A:'))
for i in range (0,n,1):
    b.append(input('Digite um valor da lista B:'))
for i in range (0,n,1):
    c.append(input('Digite um valor da lista C:'))

def crescente(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
            if cont>0:
                return True
            else:
                return False
def decrescente(lista):
    cont2=0
    for i in range (0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont2=cont2+1
    for j in range(0,len(lista)-1,1):
        p=0
        if lista[j]<lista[j+1]:
            p=p+1
        if cont2>0 and p==0:
            return True
        if cont2>0: 
            return False
def elementosiguais(lista):
    cont3=0
    for i in range (0,len(lista)-1,1):
        if lista[i]==lista[i+1] or lista[i]==lista[i-1]:
            cont3=cont3+1
            if cont3>0:
                 return True
            else:
                return False
def coin(lista):
    cont4=0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1] and lista[i]>lista[i+1]:
            cont4=cont4+1
            
if crescente(a):
    print 'S'
else:
    print 'N'

if decrescente(a):
    print 'S'
else:
    print 'N'
    
if elementosiguais(a):
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
    
if elementosiguais(b):
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
    
if elementosiguais(c):
    print 'S'
else:
    print 'N'