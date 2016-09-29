# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c:')
if a>=b and a>=c:
    print('%.2f' % a)
elif b>=a and b>=c:
    print('%.2f' % b)
else:
    print('%.2f' % c)
