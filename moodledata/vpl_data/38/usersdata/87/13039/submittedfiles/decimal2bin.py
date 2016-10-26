# -*- coding: utf-8 -*-
from __future__ import division

n=int(input("digite numero na base binaria:"))

i=0
j=1
while n!=0:
    i=i+n%10*j
    n=n/10
    j=j*2
    if n<0:
        print("%d"%i)