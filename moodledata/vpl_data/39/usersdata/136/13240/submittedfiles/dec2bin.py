# -*- coding: utf-8 -*-
from __future__ import division

n = int(input("Digite um número decimal:"))

i = 0
j = 1
d = n%2

while n>0:
    d = n%2
    n = n/2
    i = i + d*j
    j = j*10
print("%d"%i)