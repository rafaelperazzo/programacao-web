# -*- coding: utf-8 -*-
from __future__ import division

a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')

delta = (b**2)-(4*a*c)
raizdelta = (delta)**0.5

if raizdelta>0:
    x1=(-b+raizdelta)/(2*a)
    x2=(-b-raizdelta)/(2*a)
    print x1
    print x2

else:
    if raizdelta<0:
       print ("SRR")