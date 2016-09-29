# -*- coding: utf-8 -*-
from __future__ import division

#COMECE A PARTIR DAQUI!
a = input('Digite a: ')
b = input('digite b: ')
c = input('digite c: ')

delta=(b**2)-(4*a*c)

if delta >= 0:
    x1=(((-b)-(delta**(1/2.0)))/(2*a)
    x2=(-b)+(delta**0.5)/(2*a)
    print(x1)
    print(x2)
    
    else:
        print("SRR")
        