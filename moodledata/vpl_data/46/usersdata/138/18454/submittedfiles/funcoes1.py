# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range (0,n,1):
        if a[i+1]>a[i]:
            cont=cont+1
    if cont==n-1:
        return True
    else:
        return False 
n=input('digite n:')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(input('digite um valor para a:'))
for i in range(0,n,1):
    b.append(input('digite um valor para b:'))
for i in range(0,n,1):
    c.append(input('digite um valor para c:'))
if crescente(a):
    print 'S'
else:
    print 'N'
if crescente(b):
    print 'S'
else:
    print 'N'
if crescente(c):
    print 'S'
else:
    print 'N'




#escreva as demais funções





#escreva o programa principal
