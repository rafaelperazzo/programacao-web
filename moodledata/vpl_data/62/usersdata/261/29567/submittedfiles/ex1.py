# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta = (b*b) - (4ac)

if delta >=0:
    x1 = (-b+delta)/2a
    x2 = (-b-delta)/2a
    print x1
    print x2
else:
    print "SRR"