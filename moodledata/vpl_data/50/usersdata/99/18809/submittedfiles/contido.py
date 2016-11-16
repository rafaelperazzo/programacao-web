# -*- coding: utf-8 -*-
from __future__ import division

def quantidade(x,y):
    contador=0
    for i in range(0,len(y),1):
        if y[i] in x:
            contador=contador+1
    return contador
    
    
n=input('Digite a quantidade de elementos de a:')
m=input('Digite a quantidade de elementos de b:')
a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Digite um valor de a:'))


for i in range(0,m,1):
    b.append(input('Digite um valor de b:'))
    
print quantidade(a,b)