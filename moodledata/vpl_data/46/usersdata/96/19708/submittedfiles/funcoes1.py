# -*- coding: utf-8 -*-
from __future__ import division

def crescente(a):
    contador = 0
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            contador = contador + 1
    if contador==0:
        return True
    else:
        return False

def decrescente(a):
    contador = 0
    for i in range(0,len(a)-1,1):
        if a[i]<a[i+1]:
            contador = contador + 1
    if contador==0:
        return True
    else:
        return False
        
def consecutiva(a):
    contador = 0
    for i in range(0,len(a)-1,1):
        if a[i]==a[i+1] or a[i]==a[i-1]:
            contador = contador + 1
    if contador!=0:
        return True
    else:
        return False

        
a = []
b = []
c = []
n = int(input('Digite o valor de n:'))

for i in range(0,n,1):
    a.append(input('Digite o valor de a:'))
for i in range(0,n,1):
    b.append(input('Digite o valor de b:'))
for i in range(0,n,1):
    c.append(input('Digite o valor de c:'))

if crescente(a):
    print('S')
else:
    print('N')
    
if decrescente(a):
    print('S')
else:
    print('N')
    
if consecutiva(a):
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
    
if consecutiva(b):
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
    
if consecutiva(c):
    print('S')
else:
    print('N')
