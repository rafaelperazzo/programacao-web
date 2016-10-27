# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite o valor de n:')
i=0
s=0
while True:
    a=n%2
    b=n//2
    s=s+a*(10**i)
    n=b
    i=i+1
    if n==0:
        break
print(s)    