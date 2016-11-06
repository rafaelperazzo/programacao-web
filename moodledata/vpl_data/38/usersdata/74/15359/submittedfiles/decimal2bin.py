# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o numero binario: ')

j = 10
cont = 1

while n>=j:
    j = j*10
    if n>=j:
        cont = cont+1
    