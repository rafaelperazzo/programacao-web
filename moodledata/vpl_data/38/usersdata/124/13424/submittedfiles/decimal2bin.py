# -*- coding: utf-8 -*-
from __future__ import division
a = 0
c = 0
d = 0
n = int(input('Digite o valor de n: '))
p = n
while p > 0:
    p = p//10
    a = a + 1
for i in range (0, a, 1):
    d = d + (n%(10**(c+1))//(10**c))*(2**c)
    c = c + 1
print(d)