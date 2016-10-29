# -*- coding: utf-8 -*-
from __future__ import division

np = 0
ni = 0
sp = 0
si = 0
n = input('Digite o valor de n: ')
for i in range (0, n, 1):
    a = input('Digite o valor de a: ')
    if a%2 == 0:
        np = np + 1
        sp = sp + a
    elif a%2 != 0:
        ni = ni + 1
        si = si + a
print(si)
print(sp)
print(ni)
print(np)