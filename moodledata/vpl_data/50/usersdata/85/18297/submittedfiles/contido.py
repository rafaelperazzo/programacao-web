# -*- coding: utf-8 -*-
from __future__ import division

def igual(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] in b:
            cont=cont+1
    return cont
    
n= int(input('Digite o valor de n: '))
m= int(input('Digite o valor de m: '))
a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Digite o termo de a: '))

for i in range(0,m,1):
    b.append(input('Digite o termo de b: '))
    
fa= igual(a,b)

print fa