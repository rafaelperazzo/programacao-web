# -*- coding: utf-8 -*-
from __future__ import division
a = input ('digite A:')
b = input ('digite B:')
c = input ('digite C:')
d = input ('digite D:')
if a == b+c+d:
    print 'S'
    if b+c==d:
        print 'S'
        if b==c:
            print 'S'
else: 
    print 'N'
