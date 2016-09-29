# -*- coding: utf-8 -*-
from __future__ import division

p1 = input (' digite o peso do pessoa: ')
p2 = input (' digite o peso da pessoa: ')
c1 = input (' digite o comprimento do lado esquerdo da gangorra: ')
c2 = input (' digite o comprimento do lado direito da gangorra: ')

if p1*c1 == p2*c2:
    print ('Zero')
if p1*c1 >= p2*c2:
    print ('Um')
if p1*c1 =< p2*c2:
    print ('Menos Um')