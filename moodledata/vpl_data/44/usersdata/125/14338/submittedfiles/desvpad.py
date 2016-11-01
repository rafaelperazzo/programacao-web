# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('digite uma quantidade:')
a=[]

for i in range(0,n,1):
    a.append(input('digite um elemento:'))

j=0
b=0

for i in range(0,n,1):
    b=a[j]+b
    j=j+1

c=a[0]
h=a[n-1]
k=b/n

print("%.2f" %c)
print("%.2f" %h)
print("%.2f" %k)
m=0
soma=0
for i in range(0,n,1):
    soma=((a[m]-k)**2)+soma
    m=m+1
    
soma=(soma)*(1/(n-1))
soma=soma**(1/2)
print("%.2f" %soma)
