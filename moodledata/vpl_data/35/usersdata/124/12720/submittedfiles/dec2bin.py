# -*- coding: utf-8 -*-
from __future__ import division

p = int(input('Digite o valor de p: '))
q = int(input('Digite o valor de q: '))
cp = 0
cq = 0
i = 1
a = 0
while p > 0:
    p = p//10
    cp = cp + 1
while q > 0:
    p = p//10
    cq = cq + 1
d = cq - cp + 1
while i >= cp:
    a = 