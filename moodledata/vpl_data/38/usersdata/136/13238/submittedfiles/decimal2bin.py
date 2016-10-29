# -*- coding: utf-8 -*-
from __future__ import division

n = int(input("Digite um número inteiro na base binária:"))

i = 0
j = 1
while n!=0:
    i = i + n%10 * j
    n = n//10
    j = j*2
print("%d" %i)