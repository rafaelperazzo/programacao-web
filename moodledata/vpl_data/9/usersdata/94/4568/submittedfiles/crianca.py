# -*- coding: utf-8 -*-
from __future__ import division

p1=input('digite o valordo peso da criança do lado esquerdo:')
p2=input('digite o valor do peso da criança do lado direito:')
c1=input('digite o comprimento do lado esquerdo da gangorra:')
c2=input('digite o comprimento do lado direito da gangorra:')

if (p1*c1)==(p2*c2):
    print('0')
elif (p1*c1)<(p2*c2):
    print('-1')
elif (p1*c1)>(p2*c2):
    print('1')
    