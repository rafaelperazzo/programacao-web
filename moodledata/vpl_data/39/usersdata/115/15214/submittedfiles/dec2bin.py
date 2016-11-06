# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('digite um número:'))
b=n
d=0
while b>0:
    b=b//2
    d=d+1
s=0
for i in range(0,c,1):
    c=n%2
    s=s+c*(10)**i
    n=n//2
print(s)
