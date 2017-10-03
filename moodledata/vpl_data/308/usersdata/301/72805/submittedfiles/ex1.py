# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
Delta= ((b**)-4*a*c)
if Delta >= 0:
    raizdelta= Delta**0.5
    x1 = (-b+raizdelta)/(2*a)
    print(x1)
    x2 = (-b-raizdelta)/(2*a)
    print (x2)
else: 
    print('SRR)
