# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if a[i+1]>a[i]:
            cont=cont+1
    if cont==n-1:
        return True
    else:
        return False 

n=input('digite n:')
a=[]
for i in range(0,n,1):
    a.append(input('digite um valor para a:'))

if crescente(a):
    print 'S'
else:
    print 'N'
if crescente(b):
    print 'S'
else:
    print 'N'
if crescente():
    print 'S'
else:
    print 'N'






