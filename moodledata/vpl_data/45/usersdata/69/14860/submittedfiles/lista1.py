# -*- coding: utf-8 -*-
from __future__ import division
n = input('Digite o valor de n:')
a = []

for i in range(0, n, 1):
    a.append(input('Digite um elemento:'))

qim = 0
si = 0
qp=0
sp=0
for i in range(0, n, 1):
    if (a[i])%2==1:
        qim = qim+1
        si = si + a[i]
    else:
        qp=qp+1
        sp=sp+a[i]

print(si)
print(sp)
print(qim)
print(qp)
print(a)




