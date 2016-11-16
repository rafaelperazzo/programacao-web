# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if a[i]>a[i-1]:
            cont=cont+1
    if cont>0:
        return True
    else:
        return False


#escreva as demais funções


#escreva o programa principal
n=input('Digote a quantidade de elementos: ')
a=[]
'''
b=[]
c=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento de a: '))
for j in range(0,n,1):
    b.append(input('Digite um elemento de b: '))
for k in range(0,n,1):
    c.append(input('Digite um elemento de c: '))
'''    
if crescente(a):
    print 'S'
else:
    print 'N'
'''if crescente(b):
    print 'S'
else:
    print 'N'
if crescente(c):
    print 'S'
else:
    print 'N'
'''