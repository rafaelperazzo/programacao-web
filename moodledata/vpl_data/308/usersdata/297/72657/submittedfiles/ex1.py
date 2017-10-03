# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta = (b**2*4*a*c)**(0.5)
if delta >= 0 :
    x1 = (-(b)+(delta))/(2*a)
    x2 = (-(b)-(delta))/(2*a)
    print(int('x1= %.d' %x1))
    print(int('x2= %.d' %x2))
else :
    print('SRR')