# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!

delta = (b**2) - (4*a*c)

x1 = (- b + (delta)**1/2)/2*a
x2 = (- b - (delta)**1/2)/2*a

If delta >= 0:
    print (x1) and (x2)
Else:
    print ( 'SRR: Sem Raízes Reais' )
    