# -*- coding: utf-8 -*-
from __future__ import division
a = input ('digite o valor de a:')
b = input ('digite o valor de b:')
c = input ('digite o valor de c:')
d = (b**2) - (4*a*c)
xa = (-b + (d)**(1/2))/(2*a)
xb = (-b - (d)**(1/2))/(2*a)
if d<0:
    print ('a equação não possui raízes reais')
else 
    print ('%.2f' %xa)
    print ('%.2f' %xb)