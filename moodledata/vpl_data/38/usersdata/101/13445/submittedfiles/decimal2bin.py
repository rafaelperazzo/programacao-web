# -*- coding: utf-8 -*-
from __future__ import division

b = str(input('Digite um número: '))

s = 0
k = 1

while len(b) >= k:
    s = s + int(b[-k])*2**(k-1)
    k = k+1
    
print(s)