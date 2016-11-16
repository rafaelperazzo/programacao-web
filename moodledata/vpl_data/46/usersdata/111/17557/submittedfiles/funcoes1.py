# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]<=a[i+1]:
            cont = cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
    
def decrescente(lista):    
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]>=a[i+1]:
            cont = cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
    
def repet(lista):   
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]==a[i+1]:
        cont = cont+1
    if cont>=1:
        return True
    else:
        return False
    
n=input('Digite o tamanho da lista: ')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(input('Digite n1: ')
    b.append(input('Digite n2: ')
    c.append(input('Digite n3: ')
if crescente(a):
    print 'S'
else:
    print 'N'
    
if decrescente(a):
    print 'S'
else:
    print 'N'

if repeat(a):
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

if repeat(b):
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

if repeat(c):
    print 'S'
else:
    print 'N'
        




