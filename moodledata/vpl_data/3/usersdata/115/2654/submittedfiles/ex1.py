# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
n=(b**2)-4*a*c
if n>=0:
    x1=(-b+((n)**0.5))/2a
    x2=(-b-(n**0.5))/2a
    print ('x1 é %.2f' %x1)
    print ('x2 é %.2f' %x2)
else:
    print ('Não possue raizes reais')
    



