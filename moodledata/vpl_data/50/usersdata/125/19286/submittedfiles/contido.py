# -*- coding: utf-8 -*-
from __future__ import division
n=('Digite a quantidade de elementos de a:')
m=('Digite a quantidade de elementos de a:')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um valor:'))

b=[]
for i in range(0,m,1):
    a.append(input('Digite um valor:'))

cont=0    
for i in range(0,len(b),1):
    if b[i] in a:
        cont=cont+1
    


print a
print b
print cont    