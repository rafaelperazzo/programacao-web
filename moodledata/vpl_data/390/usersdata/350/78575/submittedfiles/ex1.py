# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
n = b**2
Delta = (n - ((4*a)*c))
raizdelta = Delta**0.5
if Delta < 0 :
    print('SRR')
else:
    x1 = ((-b + raizdelta)/(2*a))
    x2 = ((-b - raizdelta)/(2*a))
    print('%.2f' %x1)
    print('%.2f' %x2)
