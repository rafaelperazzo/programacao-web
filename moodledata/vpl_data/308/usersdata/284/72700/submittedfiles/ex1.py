# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!

d=((b**2)-4*a*c)
if d>=0:   
    x1=((-b+(d**0.5)/2*a))
    x2=((-b-(d**0.5)/2*a))
    print('%F.2' x1)
    print('%F.2' x2)
else :  
    print('SRR')