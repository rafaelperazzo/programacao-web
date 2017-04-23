# -*- coding: utf-8 -*-
from __future__ import division
a = int (input('Digite a: '))
b = int (input('Digite b: '))
c = int (input('Digite c: '))
#COMECE A PARTIR DAQUI!

delta = ((b*b)+(-4*a*c))
x1= (-b+(delta**1/2))/(2*a)
print('%.2f'%x1)