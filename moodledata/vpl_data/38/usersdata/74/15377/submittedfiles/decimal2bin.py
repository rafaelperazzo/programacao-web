# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o numero binario: ')

j = 10
cont = 0
d = n

while n>=2:
    if n>=j:
        cont = cont+1
    n = n/j
dec = 2**cont
d = d-j
j = 10
cont = 0
if d>=10:
    while d>=2:
        if d>=j:
            cont = cont+1
        d = d/j
else:
    dec = dec+1
dec = dec+2**cont

print('%d'% dec)