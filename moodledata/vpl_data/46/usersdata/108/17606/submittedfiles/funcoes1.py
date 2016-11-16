# -*- coding: utf-8 -*-
from __future__ import division

def crescente (l):
    for i in range (0,len(l)-2,1):
        if (l[i+1]<l[i]):
            return False
            break
        else:
            return True
    
def decrescente (l):
    for i in range (0,len(l)-2,1):
        if (l[i+1]>l[i]):
            return False
            break
        else:
            return True

def numIgual (l):
    for i in range (0,len(l)-2,1):
        if (l[i]==l[i+1]):
            return True
            break
        else:
            return False

n = input ('Digite n:')
a = []
b = []
c = []

for i in range (0,n,1):
    a.append (input ('Digite um elemento da lista a:'))
    
for i in range (0,n,1):
    b.append (input ('Digite um elemento da lista b:'))

for i in range (0,n,1):
    c.append (input ('Digite um elemento da lista c:'))

#Para a:
if crescente(a):
    print ('S')
else: 
    print ('N')
    
if decrescente(a):
    print ('S')
else: 
    print ('N')

if numIgual(a):
    print ('S')
else:
    print ('N')
    
#Para b:
if crescente(b):
    print ('S')
else: 
    print ('N')
    
if decrescente(b):
    print ('S')
else: 
    print ('N')

if numIgual(b):
    print ('S')
else:
    print ('N')

#Para c:
if crescente(c):
    print ('S')
else: 
    print ('N')
    
if decrescente(c):
    print ('S')
else: 
    print ('N')

if numIgual(c):
    print ('S')
else:
    print ('N')