# -*- coding: utf-8 -*-
from __future__ import division
import math 
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!

Delta = (b**2) - (4*a*c)

if Delta >= 0:
    x = math.sqrt(Delta)
    x1 = (- b + x)/(2*a)
    x2 = (- b - x)/(2*a)

    print (' x1=%.2f' %x1) 
    print (' x2=%.2f' %x2)

else:
    print ( 'SRR' )
    