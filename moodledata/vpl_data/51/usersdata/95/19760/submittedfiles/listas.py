# -*- coding: utf-8 -*-
from __future__ import division

n=input('Quantidade de elementos:')
lista=[]
altura=0

for i in range(0,n,1):
    lista.append(input('Digite um elemento:'))


for i in range(0,len(lista)-1,1):
    l=lista[i]-lista[i+1]
    if l<0:
        l=-l
    if l>altura:
        altura=l

print altura