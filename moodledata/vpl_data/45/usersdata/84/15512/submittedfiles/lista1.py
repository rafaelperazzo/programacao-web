# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite o valor:')
l=[]

for i in range(0,n,1):
    l.append(input('digite o numero:'))

sp=0
si=0
cp=0
ci=0
for i in range(0,n,1):
    if l[i]%2==0:
        sp=sp+(l[i])
        cp=cp+1
    else:
        si=si+(l[i])
        ci=ci+1
        
print si
print sp
print ci
print cp
print l