# -*- coding: utf-8 -*-
from __future__ import division
b=input('b')
i=0
d=0
while True:
    d=d+((b%10**(i+1))//10**i)*(2**(i+1))
    if b<<10**(i+1):
        break
print(d)
    
