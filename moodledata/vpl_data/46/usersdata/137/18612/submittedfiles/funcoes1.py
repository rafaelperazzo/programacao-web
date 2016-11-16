# -*- coding: utf-8 -*-
from __future__ import division

def crescente (a):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i]>a[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

def decrescente (a):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i]<a[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

def consecutivo (a):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i]==a[i-1] or a[i]==a[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False

n=input ('n:')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append (input('a:'))
for i in range(0,n,1):
    b.append (input('b:'))
for i in range(0,n,1):
    c.append (input('c:'))

if crescente (a):
    print ('S')
else:
    print ('N')
if decrescente (a):
    print ('S')
else:
    print ('N')
if consecutivo (a):
    print ('S')
else:
    print ('N')
    
if crescente (b):
    print ('S')
else:
    print ('N')
if decrescente (b):
    print ('S')
else:
    print ('N')
if consecutivo (c):
    print ('S')
else:
    print ('N')

if crescente (c):
    print ('S')
else:
    print ('N')
if decrescente (c):
    print ('S')
else:
    print ('N')
if consecutivo (c):
    print ('S')
else:
    print ('N')
