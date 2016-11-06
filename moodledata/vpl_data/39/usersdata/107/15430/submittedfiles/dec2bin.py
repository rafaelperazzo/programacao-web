# -*- coding: utf-8 -*-
from __future__ import division
b = int(input('Digite um valor:')
q = b
cont = 0
while q>0:
    q = q//2
    cont = cont + 1
s = 0
for i in range(0, cont, 1):
    a = b%2
    s = s + a*(10)**i
    b = b//2
print(s)