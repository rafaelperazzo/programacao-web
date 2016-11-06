# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o numero binario: ')

j = 10
k = 10
l = 10
cont = 0
cont1 = 0
d = n

while n>2:
    if n>=j:
        cont = cont+1
    n = n/j
    l = l*10
    if d<=l:
        
        i = l/10
        d = d-i
        while d>2:
            if d>=k:
                cont1 = cont1+1
            d = d/k

dec = 2**cont+2**cont1



print('%d'% dec)