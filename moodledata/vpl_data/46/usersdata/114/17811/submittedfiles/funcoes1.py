# -*- coding: utf-8 -*-
from __future__ import division

def crescente (l):
    cont=0
    for i in range(0,len(l)-1,1):
        if l[i]>l[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
        
def decrescente (l):
    cont=0
    for i in range(0,len(l)-1,1):
        if l[i]<l[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
            
def elementos_iguais (l):
    cont=0
    for i in range(0,len(l)-1,1):
        if l[i]==l[i+1]:
            cont=cont+1
    if cont!=1:
        return True
    else:
        return False
n=input('digite o número de elementos: ')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(input('digite os elementos da lista a: '))
for i in range(0,n,1):
    b.append(input('digite os elementos da lista b: '))
for i in range(0,n,1):
    c.append(input('digite os elementos da lista c: '))
if crescente(a):
    print ('S')
else:
    print ('N')

if decrescente(a):
    print ('S')
else:
    print ('N')

if elementos_iguais(a):
    print ('S')
else:
    print ('N')    
    
if crescente(b):
    print ('S')
else:
    print ('N')

if decrescente(b):
    print ('S')
else:
    print ('N')
    
if elementos_iguais(b):
    print ('S')
else:
    print ('N') 
    
if crescente(c):
    print ('S')
else:
    print ('N')  

if decrescente(c):
    print ('S')
else:
    print ('N') 
    
if elementos_iguais(c):
    print ('S')
else:
    print ('N')    