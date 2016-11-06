# -*- coding: utf-8 -*-
from __future__ import division

b = int(input('digite um numero: '))

d = int(b/2)
r = int(r%2)
f = str(r)

while d != 0:
    b = d
    d = int(b/2)
    r = int(r%2)
    f = str(r) + f
    
print int(f)