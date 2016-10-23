# -*- coding: utf-8 -*-
from __future__ import division

p = int(input('Digite o valor de p: '))
cp = 0
while p > 0:
    p = p//10
    cp = cp + 1
print(cp)