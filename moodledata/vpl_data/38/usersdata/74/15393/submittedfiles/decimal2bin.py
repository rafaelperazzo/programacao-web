# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o numero binario: ')

j = 10
cont = 0
cont1 = 0

while n>=j:
    if n>=j:
        cont = cont+1
    j = j*10
    dec = 2**cont


print('%d'% dec)