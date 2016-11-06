# -*- coding: utf-8 -*-
from __future__ import division
n = int(input('Dgite um número:'))
p = n
c = 0
while p>0:
    p = p//2
    c = c + 1
s = 0
for i in range(0, c, 1):
    b = n%2
    s = s + b*(10)**i
    n = n//2
print(s)
