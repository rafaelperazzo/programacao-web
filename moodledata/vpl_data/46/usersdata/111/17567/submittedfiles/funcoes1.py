# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]<a[i+1]:
            cont = cont+1
    if cont==len(lista):
        return True
    else:
        return False
    
def decrescente(lista):    
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            cont = cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
    
def repeat(lista):   
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
    a.append(input('Digite n1: '))
for j in range(0,n,1):
    b.append(input('Digite n2: '))
for k in range(0,n,1):
    c.append(input('Digite n3: '))
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




