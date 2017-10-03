# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
delta= (b*b)-(4*a*c)
if delta<0:
    print('SRR')
if delta>=0:
    x1= (-b+((delta)**(1/2)))/2*a
    x2= (-b-((delta)**(1/2)))/2*a
    print(x1)
    print(x2)
    