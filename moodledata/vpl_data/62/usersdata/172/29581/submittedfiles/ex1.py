# -*- coding: utf-8 -*-
from __future__ import division
a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))
#COMECE A PARTIR DAQUI!
d = (b**2)-4*a*c
if  d>=0:
    x1=(-b+((d)**0.5))/2*a
    x2=(-b-((d)**0.5))/2*a
    print('%.2f'%x1)
    print('%.2f'%x2)
else    :
    print('SRR')
    