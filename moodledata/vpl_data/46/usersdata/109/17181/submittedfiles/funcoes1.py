# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range (0,n,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==n:
        return True
    else:
        return False

#escreva as demais funções

def desrescente(lista):
    cont=0
    for i in range (0,n,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==n:
        return True
    else:
        return False
    
    
def consecultivos(lista):
    cont=0
    for i in range (0,n,1):
        if lista[i]==(1+a[i+1]):
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
    
if crescente(a):
    print 'S'
else:
    print 'N'
if  decrescente(a):
     print 'S'
else:
    print 'N'    
if consecultivos(a):
     print 'S'
else:
    print 'N'
if crescente(b):
     print 'S'
else:
    print 'N'
if decrescente(b):
     print 'S'
else:
    print 'N'
if consecultivos(b):
     print 'S'
else:
    print 'N'
if crescente(c):
     print 'S'
else:
    print 'N'
if decrescente(c):
     print 'S'
else:
    print 'N'
if consecultivos(c):
     print 'S'
else:
    print 'N'


