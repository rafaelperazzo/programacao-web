# -*- coding: utf-8 -*-
from __future__ import division

p = int(input('Digite o valor de p: '))
q = int(input('Digite o valor de q: '))
cp = 0
cq = 0
i = 1
a = 0
fp = p
fq = q
while fp > 0:
    fp = fp//10
    cp = cp + 1
while fq > 0:
    fq = fq//10
    cq = cq + 1
while True:
    if (q//(10**a))%(10**cp) == p:
        print('S')
        break
    else:
        a = a + 1
        if a == cq:
            print('N')
            break
print(p)
print(q)
print(cp)
print(cq)
print(a)