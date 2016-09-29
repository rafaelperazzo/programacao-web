# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!

Delta = (b**2) - (4*a*c)

if Delta >= 0:
    x1 = float(- b + ((Delta)**0.5))/(2*a)
    x2 = float(- b - ((Delta)**0.5))/(2*a)

    print (' x1=%.2f' %x1) 
    print (' x2=%.2f' %x2)

else:
    print ( 'SRR' )
    