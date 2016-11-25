# -*- coding: utf-8 -*-
from __future__ import division

def crescente(a):
    contador = 0
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            contador contador + 1
    if contador==0:
        return True
    else:
        return False

def decrescente(a):
    contador = 0
    for i in range(0,len(a)-1,1):
        if a[i]<a[i+1]:
            contador contador + 1
    if contador==0:
        return True
    else:
        return False
        
a = []
b = []
c = []
n = input('n:')

for i in range(0,n,1):
    a.append(input('a:'))
for i in range(0,n,1):
    a.append(input('b:'))
for i in range(0,n,1):
    a.append(input('c:'))

if crescente(a):
    print('S')
else:
    print('N')
    
if decrescente(a):
    print('S')
else:
    print('N')
    
if consecutivo(a):
    print('S')
else:
    print('N')

if crescente(b):
    print('S')
else:
    print('N')
    
if decrescente(b):
    print('S')
else:
    print('N')
    
if consecutivo(b):
    print('S')
else:
    print('N')
    
if crescente(c):
    print('S')
else:
    print('N')
    
if decrescente(c):
    print('S')
else:
    print('N')
    
if consecutivo(c):
    print('S')
else:
    print('N')
