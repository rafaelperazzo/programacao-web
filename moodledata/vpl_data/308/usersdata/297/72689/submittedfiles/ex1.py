# -*- coding: utf-8 -*-
from __future__ import division
a = input(int('Digite a: '))
b = input(int('Digite b: '))
c = input(int('Digite c: '))
#COMECE A PARTIR DAQUI!
Delta = ((b**2)*(-4)*a*c)**(0.5)
x1 = (-b+(Delta))/(2*a)
x2 = (-b-(Delta))/(2*a)
if Delta>=0 :
    print('X1 = %d' % x1 )
    print('X2 = %d' % x2 )
else :
    print('SRR')