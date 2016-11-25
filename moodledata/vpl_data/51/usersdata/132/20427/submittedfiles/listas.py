# -*- coding: utf-8 -*-
from __future__ import division
def deg(lista):
    maior=0
    for i in range(0,len(lista)-1,1):
        if lista[i+1]>=lista[i]:
            d=lista[i+1]-lista[i]
            if d>=maior:
                maior=d
        if lista[i+1]<=lista[i]:
            d=lista[i]-lista[i+1]
            if d>=maior:
                maior=d
    return maior            
a=[]
n=input('digite a quantidade de termos da lista:')
for i in range(0,n,1):
    a.append(input('digite os termos:'))
c=deg(a)
print(c)
