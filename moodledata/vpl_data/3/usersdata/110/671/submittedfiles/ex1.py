# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite a: ')
b=input(' Digite b: ')
c=input( ' Digite c: ')
if a<=b and b<=c:
    print('%.2f'%c)
if a<=c and c<=b :
    print('%.2f'%b)
if c<=b and b<=a:
    print('%.2f'%a)
