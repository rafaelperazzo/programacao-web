# -*- coding: utf-8 -*-
from __future__ import division
#COMECE A PARTIR DAQUI!
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))

delta= b**2 -4*a*c
x1=(-b+(delta**(1/2)))/(2*a)
x2=(-b-(delta**(1/2)))/(2*a)

if delta>=0:
    print ("x1 = ",x1)
    print ("x2 = ",x2)
else:
    print ('SRR')
