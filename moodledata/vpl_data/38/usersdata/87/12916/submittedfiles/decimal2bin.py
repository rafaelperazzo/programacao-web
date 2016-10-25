# -*- coding: utf-8 -*-
from __future__ import division

n=input("digite valor do numero binario:")

i=0
j=1

while n!=0:
    i=i + n%10 * j
    n=n/10
    j=2**j
print(i)