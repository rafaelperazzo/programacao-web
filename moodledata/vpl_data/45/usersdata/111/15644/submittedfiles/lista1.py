# -*- coding: utf-8 -*-
from __future__ import division

n=input('tamanho da lista: ')

lista=[2,3,4,5]
print lista[0]
cont=0
cont2=0
for i in range (0,n,1):
    num=input('num:')
    lista.append(num)
    if lista[i]%2==0:
        cont = cont + 1
    else:
        cont2=cont2+1
print cont
print cont 2
        
    