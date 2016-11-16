# -*- coding: utf-8 -*-
from __future__ import division

def contido(x,y):
    cont=0
    for i in range(0,len(y),1):
        if y[i] in x:
            cont=cont+1
        return cont
        
n=input('digite a quantidade de elementos de a:')
m=input('digite a quantidade de elementos de b:')

a=[]
for i in range(0,n,1):
    a.append(input('digite a lista a:')

b=[]
for i in range(0,m,1):
     b.append(input('digite a lista b:')
     
print contido(a,b)