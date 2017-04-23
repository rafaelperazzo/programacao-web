# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
DELTA=(b**2)-4*a*c
if DELTA>=0:
    X1=(-b+DELTA**(1/2))/2*a
    print('X1 é %'%X1)
    X2=(-b-DELTA**(1/2))/2*a
    elif DELTA<0:
        print('SRR')

