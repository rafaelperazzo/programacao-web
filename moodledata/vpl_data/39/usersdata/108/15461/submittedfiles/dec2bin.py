# -*- coding: utf-8 -*-
from __future__ import division

n = int( input ('Digite n:'))
i = 0
a = 0
b = 0


while (n>=1):
    a = n%2
    b = b+(a*(10**i))
    n = n//2
    i = i+1
    
print(b)


