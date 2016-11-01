# -*- coding: utf-8 -*-
from __future__ import division

a = input('')
b = input('')
c = input('')

ma = 0
mb = 0

if c%a==0 or c%b==0:
    if c%a==0:
        ma = c/a
        print('%d %d'% (ma,mb))
    elif c%b==0:
        mb = c/b
        print('%d %d'% (ma,mb))