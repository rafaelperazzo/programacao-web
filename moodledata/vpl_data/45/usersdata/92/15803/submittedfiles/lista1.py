# -*- coding: utf-8 -*-
from __future__ import division

n= int(input('Digite um valor: '))

x= []
for i in range(0, n, 1):
    x.append(input('Digite um valor: '))
    
somai=0    
for i in range(0, n, 1):
    if (x[i]%2)!=0:
        somai= somai + x[i]
        
somap=0    
for i in range(0, n, 1):
    if (x[i]%2)==0:
        somap= somap + x[i]

conti=0    
for i in range(0, n, 1):
    if (x[i]%2)!=0:
        conti= conti + 1

contp=0    
for i in range(0, n, 1):
    if (x[i]%2)==0:
        contp= contp + 1

print somai
print somap
print conti
print contp
print x
