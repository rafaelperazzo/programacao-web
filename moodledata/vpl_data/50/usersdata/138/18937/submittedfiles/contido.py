# -*- coding: utf-8 -*-
from __future__ import division

def congruencia(a,b):
    cont=0
    for i in range(0,len(a),1):
        for z in range(0,len(b),1):
            if a[i]==b[z]:
                cont=cont+1
    return cont
n=input('quantidade de elementos de a:')
m=input('quantidade de elementos de b:')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('digite um elemento para a:'))
for i in range(0,m,1):
    b.append(input('digite um elemento para b:'))
c=congruencia(a,b)
print c
    

