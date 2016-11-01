# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite o valor de n: ')
lista=[]

for i in range (0,n,1):
    lista.append(input('digite um valor: '))
    
soma=lista[0]
for i in range (1,n,1):
    soma=soma + lista[i] 
media=soma/n

print ('%.2f' %lista[0])
print ('%.2f' %lista[n-1])
print ('%.2f' %media)
print ('%.2f' %lista)