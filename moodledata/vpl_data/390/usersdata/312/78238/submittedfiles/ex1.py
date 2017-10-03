# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
Delta = b**2-4*a*c
print 'Delta: ',Delta
if Delta >= 0:
    x1 = (-b+Delta**0.5)/2*a
    x2 = (-b-Delta**0.5)/2*a
    print( x1,x2)
else:
    if Delta < 0:
        print 'SRR'
    