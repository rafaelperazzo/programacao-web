# -*- coding: utf-8 -*-
from __future__ import division

def quant(x,y):
    cont=0
    for i in range(0,len(x),1):
        if x[i] in y:
            cont=cont+1
    return cont
    
n= inout('n:')
m= input('m:')
a=[]
b=[]

for i in range(0,n,1):
    a.append(input('a:'))
    
for i in range(0,m,1):
    b.append(input('b:'))

print (quant(a,b))