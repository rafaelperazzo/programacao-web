# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
Delta = (b**2)-4*a*c
if Delta >= 0:
    X1 = (-b+(Delta**0.5))/2*a
    X2 = (-b-(Delta**0.5))/2*a
else:
    print("SRR")