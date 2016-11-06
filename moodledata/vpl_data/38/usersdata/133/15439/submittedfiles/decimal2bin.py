# -*- coding: utf-8 -*-
from __future__ import division
n = int(input('Digite um valor:'))
p = n
c = 0
while p>0:
    p = p//10
    c = c + 1
s = 0
for i in range(0, c, 1):
    b = n%10
    s = s + b*(2)**i
    n = n//10
print(s)
