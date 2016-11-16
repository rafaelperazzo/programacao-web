# -*- coding: utf-8 -*-
from __future__ import division
defr teste(lista1, lista2):
    c=0
    for i in range(0,len(lista),1):
        if lista2 in lista1:
            c=c+1
    return c        
a=[]
b=[]
n=input('digite a quantidade de termos de a:')
m=input('digite a quantidade de termos de b:')
for i in range(0,n,1):
    a.append(input('digite os termos de a:'))
for i in range(0,m,1):
    b.append(input('digite os termos de b:'))
z=teste(a,b)
print(z)