# -*- coding: utf-8 -*-
from __future__ import division
p1 = input ('digite o peso 1:')
c1 = input ('comprimento 1:')
p2 = input ('digite o peso 2:')
c2 = input ('comprimento 2:')
if p1*c1 == p2*c2:
    print '0'
elif p1*c1> p2*c2:
        print '-1'
else:
        print '1'
