# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite a quantidade de valores:')
a=[]

for i in range(0,n,1):
    a.append(input('digite um elemento:'))
    
j=0
b=0

for i in range (0,n,1):
    b=a[j]+b
    j=j+1
    
e=a[0]
d=a[n-1]
f=b/n

print(e)
print(d)
print(f)

    
    
