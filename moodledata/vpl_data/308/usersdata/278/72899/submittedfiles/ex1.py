# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
A = b**2 -4*a*c
if A>=0:
    x1 = (-b + (A)**(1/2))/2*a
    print("%.2f" %(x1))
    x2 = (-b - (A)**(1/2))/2*a
    print("%.2f" %(x2))
else:
    print("SRR")
