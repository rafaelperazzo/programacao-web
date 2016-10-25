# -*- coding: utf-8 -*-
from __future__ import division

n=input("numero decimal:")

i=0
j=1

while n>0:
    n=n%2
    n=n/2
    i=i+n*j
    j=j*10
print(i)
    