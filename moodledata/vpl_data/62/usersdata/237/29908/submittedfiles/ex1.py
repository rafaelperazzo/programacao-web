# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
Delta = (b*b)-(4*a*c)
if Delta>=0 :
    x=(-b+(Delta**(1/2)))/(2*a)
    y=(-b-(Delta**(1/2)))/(2*a)
    print("%.2f" % x)
    print("%.2f" % y)
else:('SRR')