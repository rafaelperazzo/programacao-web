# -*- coding: utf-8 -*-
from __future__ import division
def contido(a,b):
    cont=0
    for i in range(0,len(b),1):
        if b[i] in a:
            cont+=1
    return cont
    
a=[]
b=[]
a=input('digite a quantidade de a:')
b=input('digite a quantidade de b:')

for i in range(0,n,1):
    a.append(input('digite a:'))
for i in range(0,n,1):
    b.append(input('digite b:'))
    
print contido(a,b)
