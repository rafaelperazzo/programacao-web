# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range (0,n,1):
        if a[i]<a[i+1]:
            cont=cont+1
    if cont==n:
        return True
    else:
        return False

#escreva as demais funções

def desrescente(lista):
    cont=0
    for i in range (0,n,1):
        if a[i]<a[i+1]:
            cont=cont+1
    if cont==n:
        return True
    else:
        return False
    
    
def consecultivos(lista):
    cont=0
    for i in range (0,n,1):
        if a[i]==(1+a[i+1]):
            cont=cont+1
    if cont==n:
        return True
    else:
        return False

    

#escreva o programa principal

n=input('Digite o tamanho da lista:')
a=[]
b=[]
c=[]
for i in range (0,n,1):
    a.append(input('Digite um valor para a lista a:'))
for i in range (0,n,1):
    b.append(input('Digite um valor para a lista b:'))
for i in range (0,n,1):
    c.append(input('Digite um valor para a lista c:'))
    
if print crescente(a):
    print 'S'
elif:
    print 'N'
if print decrescente(a):
     print 'S'
elif:
    print 'N'    
if print consecultivos(a):
     print 'S'
elif:
    print 'N'
if print crescente(b):
     print 'S'
elif:
    print 'N'
if print decrescente(b):
     print 'S'
elif:
    print 'N'
if print consecultivos(b):
     print 'S'
elif:
    print 'N'
if print crescente(c):
     print 'S'
elif:
    print 'N'
if print decrescente(c):
     print 'S'
elif:
    print 'N'
if print consecultivos(c):
     print 'S'
elif:
    print 'N'


