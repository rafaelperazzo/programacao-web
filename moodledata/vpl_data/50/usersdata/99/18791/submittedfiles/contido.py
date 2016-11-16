# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de elementos de a:')
m=input('Digite a quantidade de elementos de b:')
a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Digite um valor para a:'))
    
for i in range(0,m,1):
    b.append(input('Digite um valor para b:'))
    
contador=0
for i in range(0,len(b),1):
    if b[i] in a:
        contador = contador+1