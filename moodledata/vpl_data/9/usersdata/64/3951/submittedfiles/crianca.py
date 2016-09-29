# -*- coding: utf-8 -*-
from __future__ import division

p1 = input('Digite o peso 1: ')
c1 = input('Digite o peso 1: ')
p2 = input('Digite o peso 2: ')
c2 = input('Digite o peso 2: ')

if p1*c1 == p2*c2:
    print "'0'"
if p1*c1 < p2*c2:
    print "'-1'"
if p1*c1 > p2*c2:
    print "'1'"
