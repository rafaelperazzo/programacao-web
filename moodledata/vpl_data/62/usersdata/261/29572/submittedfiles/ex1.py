# -*- coding: utf-8 -*-
from __future__ import division
a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))
#COMECE A PARTIR DAQUI!
delta = ((b*b) - (4*a*c))**(1/2)

if delta >=0:
    x1 = (-b+delta)/2*a
    x2 = (-b-delta)/2*a
    print (x1)
    print (x2)
else:
    print ("SRR")