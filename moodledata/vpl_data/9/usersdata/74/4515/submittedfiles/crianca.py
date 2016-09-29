# -*- coding: utf-8 -*-
from __future__ import division

p1 = input('')
c1 = input("')
p2 = input('')
c2 = input('')

if (p1*c1)=(p2*c2):
    print('0')
elif (p1*c1)>(p2*c2):
    print('-1')
elif (p2*c2)>(p1*c1):
    print('1')