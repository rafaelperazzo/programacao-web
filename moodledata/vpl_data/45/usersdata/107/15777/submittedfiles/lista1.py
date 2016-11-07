# -*- coding: utf-8 -*-
from __future__ import division
n = input('Digte o valor de n:')
a = []
for i in range(0, n, 1):
    a.append(input('digite um número:'))
si = 0
sp = 0
conti = 0
contp = 0
for i in range(0, n, 1):
    if (a[i]%2==0):
        sp = sp + a[i]
        contp = contp + 1
    else:
        si = si + a[i]
        conti = conti + 1

print(si)
print(sp)
print(conti)
print(contp)
print(a)