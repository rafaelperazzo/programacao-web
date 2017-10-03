# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!

#Entradas
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))

D = (b**2)-4*a*c
if D < 0:
    x1 = ((b**2)+(D**0.5))/2*a
    x2 = ((b**2)-(D**0.5))/2*a
    print ('x1 = %f'%x1)
    print ('x2 = %f'%x2)