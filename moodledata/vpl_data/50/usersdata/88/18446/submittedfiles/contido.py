# -*- coding: utf-8 -*-
from __future__ import division

def f1(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i] in lista:
            cont=cont+1
    if cont>0:
        return True
    else:
        return False

n=input('Digite a quantidade de elementos de a: ')
m=input('Digite a quantidade de elementos de b: ')

a=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento de a: '))
b=[]
for i in range(0,m,1):
    b.append(input('Digite um elemento de b: '))
    
if f1(b):
    print cont
            



