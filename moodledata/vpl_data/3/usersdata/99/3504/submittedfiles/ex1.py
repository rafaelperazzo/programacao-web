# -*- coding: utf-8 -*-
from __future__ import division

#COMECE A PARTIR DAQUI!
a = input('Digite o valor de a:')
b = input('Digite o valor de b:')
c = input('Digite o valor de c:')

delta=((b**2)-(4*a*c))

if (delta>=0):
    x1=(-b+(delta**1/2))/2*a
    x2=(-b-(delta**1/2))/2*a
    print ('x1=%.2f'%x1)
    print ('x2=%.2f'%x2)
else:
    print ('SRR')

    