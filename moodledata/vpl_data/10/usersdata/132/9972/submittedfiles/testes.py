# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite um numero:')
i=1
x=i*(i+1)*(i+2)
while True:
    if x==a:
        print('s')
        break
    if x>a:
        print('n')
        break
i=i+1    