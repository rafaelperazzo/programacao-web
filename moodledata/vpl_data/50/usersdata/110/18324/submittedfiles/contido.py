# -*- coding: utf-8 -*-
from __future__ import division

def contido(a,b):
   cont=0
    for i in range(0,len(b),1):
        if b[i] in a:
            cont=cont+1
    return cont
n=input('Digite n: ')
m=input('Digite m : ')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('Digite valor de a: '))
for i in range (0,m,1):
    b.appende(input('Digite valor de b: '))
print(contido(a,b))