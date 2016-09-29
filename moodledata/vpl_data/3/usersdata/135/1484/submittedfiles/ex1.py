# -*- coding: utf-8 -*-
from __future__ import division
a =float( input('Digite a: '))
b =float( input('Digite b: '))
c =float( input('Digite c: '))

Delta=(b**2)-(4*a*c)
if Delta <0:
    print 'SRR'
if Delta>=0:
    raizdeDelta= Delta**0.5
x1= -b+raizdeDelta/(2*a)
x2= -b-raizdeDelta/(2*a)
print 'x1=%.0f'%x1
print 'x2=%.0f'%x2

