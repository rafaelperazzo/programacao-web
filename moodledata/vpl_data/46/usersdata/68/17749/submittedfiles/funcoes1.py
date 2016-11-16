# -*- coding: utf-8 -*-
from __future__ import division

#programa principal
n=input('Digite n:')
a=[]
b=[]
c=[]
for i in range (0,n,1):
    a.append (input('Digite um elemento da lista a:'))
for i in range (0,n,1):
    b.append (input('Digite um elemento da lista b:'))
for i in range (0,n,1):
    c.append (input('Digite um elemento da lista c:'))
    
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

#defcrescente
cont=0
for i in range (0, len(a)-1,1):
    if a[i]>a[i+1]:
        cont=cont+1
if cont==0:
    return True
else:
    return False

#defdecrescente
cont=0
for i in range (0,len(a)-1,1):
    if a[i]<a[i+1]:
        cont=cont+1
if cont==0:
    return True
else:
    return False
#defelementos iguais

cont=0
for i in range (0,len(a)-1,1):
    if a[i]==a[i+1]:
        cont=cont+1
if cont==0:
    return True
else:
    return False