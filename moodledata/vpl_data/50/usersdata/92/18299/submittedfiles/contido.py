# -*- coding: utf-8 -*-
from __future__ import division

n= input('Digite n: ')
m= input('Digite m: ')

a=[]
for i in range(0, n, 1):
    a.append(input('Digite um valor de a: '))

b=[]
for i in range(0, m, 1):
    b.append(input('Digite um valor de b: '))

def  contidos(x,y):
    cont=0
    for i in range(0, len(y), 1):
        if y[i] in x:
            cont= cont+ 1
    return cont
    
print contidos(a,b)

