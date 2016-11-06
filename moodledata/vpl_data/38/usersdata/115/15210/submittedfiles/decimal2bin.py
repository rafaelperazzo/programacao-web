# -*- coding: utf-8 -*-
from __future__ import division
n=input('digite um número:')
b=n
d=0
while b>0:
    b=b//10
    d=d+1
s=0
for i in range(0,d,1):
    c=n%10
    s=s+c*(2)**i
    n=n//10
print(s)
