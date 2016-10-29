# -*- coding: utf-8 -*-
from __future__ import division
a = 0
b = 0
n = input('Digite o valor de n: ')
while n//2 > 0:
    b = b + (10**(a))
    n = n//2
    a = a + 1
print(b)