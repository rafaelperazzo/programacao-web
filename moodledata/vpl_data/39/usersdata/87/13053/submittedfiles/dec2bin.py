# -*- coding: utf-8 -*-
from __future__ import division

n=int(input("numero decimal:"))

i=0
j=1
d=n%2

while n>0:
    d=n%2
    n=n/2
    i=float(i+d*j)
    j=j*10
print(i)

