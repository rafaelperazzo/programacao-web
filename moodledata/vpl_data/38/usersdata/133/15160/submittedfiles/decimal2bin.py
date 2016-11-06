# -*- coding: utf-8 -*-
from __future__ import division
n = input('Digite um valor:')
p = n
c = 0
whilw p>0:
    p = p//10
    c = c + 1
s = 0
for i in range(0, c, 1):
    b = n%10
    s = s + b*(math.pow(2, i))
    a = a//10
print(s)
