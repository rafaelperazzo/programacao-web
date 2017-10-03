# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta=((b**2)-4*a*c)
if delta >= 0:
    rd=delta**0.5
    x1=(-b+rd)/(2*a)
    x2=(-b-rd)/(2*a)
    print(x1)
    print(x2)
else:
    print('SRR')
