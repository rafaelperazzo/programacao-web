# -*- coding: utf-8 -*-
from __future__ import division

def contido(a,b):
    cont=0
    for i in range(0,len(b),1):
        if b[i] in a:
            cont=cont+1
    return cont
    

n=input('digite a quantidade de elementos de a:')
m=input('digite a quantidade de elementos de b:')

a=[]
for i in range(0,n,1):
    a.append(input('digite os elementos de a:'))
    
b=[]
for i in range(0,m,1):
    b.append(input('digite os elementos de b:'))
    
print contido(b,a)