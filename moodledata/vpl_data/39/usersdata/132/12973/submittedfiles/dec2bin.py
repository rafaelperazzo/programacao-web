# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('digite o numero:'))
c=1
y=n
while(y//2!=0):
    c=c+1
    y=y//2
x=0
s=0
w=n
while(x<=c-1):
    p=w%2*10**x
    s=s+p
    w=w//2
    x=x+1
print(s)    