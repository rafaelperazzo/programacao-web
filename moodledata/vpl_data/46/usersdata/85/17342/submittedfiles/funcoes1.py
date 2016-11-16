# -*- coding: utf-8 -*-
from __future__ import division

def crescente(a):
    cont=0
    if a[0]<a[1]:
        cont=cont+1
    if a[len(a)-1]>a[len(a)-2]:
        cont=cont+1
    for i in range(1,len(a)-1,1):
        if a[i]<a[i+1]:
            cont= cont+1
    if cont==len(a):
        return True
    else:
        return False

def decrescente(a):
    cont1=0
    if a[0]>a[1]:
        cont1=cont1+1
    if a[len(a)-1]<a[len(a)-2]:
        cont1=cont1+1
    for i in range(1,len(a)-1,1):
        if a[i]>a[i+1]:
            cont1=cont1+1
    if cont1==len(a):
        return True
    else:
        return False

def consecutivo(a):
    cont2=0
    for i in range(0,len(a)-1,1):
        if a[i]==a[i+1]:
            cont2=cont2+1
    if cont2>0:
        return True
    else:
        return False

n= int(input('Digite o valor de n: '))
a=[]
b=[]
c=[]

for i in range(0,n,1):
    a.append(input('Digite o termo de a: '))

for i in range(0,n,1):
    b.append(input('Digite o termo de b: '))
    
for i in range(0,n,1):
    c.append(input('Digite o termo de c: '))

#Para A    
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
#Para B
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
#Para C
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