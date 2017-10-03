# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
Delta = ((b**2)*(-4)*a*c)**(0.5)
X1 = (-b+(Delta))/(2*a)
X2 = (-b-(Delta))/(2*a)
if Delta>=0 :
    print(int('X1= %.d' %X1 ))
    print(int('X2= %.d' %X2 ))
else :
    print('SRR')