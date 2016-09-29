# -*- coding: utf-8 -*-
from __future__ import division]
p1=input('digite o peso do lado esquerdo:')
c1=input('digite o comprimento do lado esquerdo:')
p2=input('digite o peso do lado direito:')
c2=input('digite o comprimento do lado direito:')

p1*c1=p2*c2

if p1*c1==p2*c2:
    print('0')
if p1*c1<p2*c2:
    print('-1')
if p1*c1>p2*c2:
    print('1')
