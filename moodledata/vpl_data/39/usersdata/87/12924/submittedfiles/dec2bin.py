# -*- coding: utf-8 -*-
from __future__ import division

n=input("numero decimal:")

i=0
j=1
w=0

while n>0:
    w=n%2
    n=n/2
    i=i+w*j
    j=j*10
print(i)
    