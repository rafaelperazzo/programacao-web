# -*- coding: utf-8 -*-
from __future__ import division
b=input('b')
i=0
d=0
while True:
    d=d+((b%10**(i+1))//10**i)*(2**i)
    
    if b<10**(i+1):
        break
    i=i+1
print(d)
    
