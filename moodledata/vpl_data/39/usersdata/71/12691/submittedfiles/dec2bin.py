# -*- coding: utf-8 -*-
from __future__ import division

d=input()
di=d
n=1
soma=0

while di//2>0:
    n=n+1
    di=di//2

for i in range (0,n,1):
    b=(d%2)*(10**i)
    soma=soma+b
    d=d//2
    
print soma