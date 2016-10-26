# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('digite o numero:'))
c=0
i=1
while(n//i!=0):
    c=c+1
    i=i*10
x=0
s=0
y=n
while(x<=c-1):
    p=y%10*2**x
    s=s+p
    x=x+1
    y=y//10
print(s)    