# -*- coding: utf-8 -*-
from __future__ import division

a = input('Valor da primeira moeda: ')
b = input('Valor da segunda moeda: ')
c = input('Valor da terceira moeda: ')

ma = 0
mb = 0

if c%a==0 or c%b==0:
    if c%a==0 and c%b==0:
        c1 = c-2*b
        c2 = c-2*a
        if c1%a==0:
            ma = c1/a
            mb = 2
            print('%d %d'% (ma,mb))
        elif c2%b==0:
            ma = 2
            mb = c2/b
            print('%d %d'% (ma,mb))
    if c%a==0:
        ma = c/a
        print('%d %d'% (ma,mb))
    if c%b==0:
        mb = c/b
        print('%d %d'% (ma,mb))
else:
    print('N')