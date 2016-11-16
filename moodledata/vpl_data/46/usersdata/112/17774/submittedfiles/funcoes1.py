# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de números das listas:')
a=[]
b=[]
c=[]
for i in range (0,n,1):
    a.append(input('Digite um valor da lista A:'))
for i in range (0,n,1):
    b.append(input('Digite um valor da lista B:'))
for i in range (0,n,1):
    c.append(input('Digite um valor da lista C:'))

def crescente(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
            if cont>0:
                return True
            else:
                return False
if crescente(a):
    print 'S'