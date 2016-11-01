# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite o valor de n: ')
lista=[]

for i in range (0,n,1):
    lista.append(input('digite um valor: '))
    
media=lista[0]
for i in range (1,n,1):
    media=media + lista[i] 
soma=media/n
print lista[0]
print lista[n-1]
print soma
print lista