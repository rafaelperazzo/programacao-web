# -*- coding: utf-8 -*-
from __future__ import division

n=input('tamanho da lista: ')

lista=[]

cont=0
cont2=0
a=0
b=0
for i in range (0,n,1):
    num=input('num:')
    lista.append(num)
    if lista[i]%2==0:
        a = a + lista[i]
        cont = cont + 1
    else:
        b=b+lista[i]
        cont2=cont2+1
print cont
print cont2
print a
print b
        
    