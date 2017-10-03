# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
delta = (b**b)-4*a*c
if delta<0:
    print("SRR")
if delta>0:
    raizdelta=(delta**0.5)
    X1 = -b+raizdelta/(2*a)
    X2 = -b-raizdelta/(2*a)
    print('%.1f'% X1)
    print('%.1f' % X2)
if delta==0:
    print('%.1f'% X1)
    print('%.1f' % X2)

        


