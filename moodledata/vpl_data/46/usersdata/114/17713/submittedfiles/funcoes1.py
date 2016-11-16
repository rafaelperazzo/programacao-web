# -*- coding: utf-8 -*-
from __future__ import division

def crescente (l):
    for i in range(0,n,1):
        if l[0]<l[1] and l[i-1]<l[i]<l[i+1] and l[len(l)-1]>l[len(l)-2]:
            return True
        else:
            return False
def decrescente (l):
    for i in range(0,n,1):
        if l[0]>l[1] and l[i-1]>l[i]>l[i+1] and l[len(l)-1]<l[len(l)-2]:
            return True
        else:
            return False
def elementosiguais (l):
    for i in range(0,n,1):
        if l[i]==l[i-1] or l[i]==l[i+1]:
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

if elementosiguais(a):
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
    
if elementosiguais(b):
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
    
if elementosiguais(c):
    print ('S')
else:
    print ('N')    