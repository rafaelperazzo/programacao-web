# -*- coding: utf-8 -*-
from __future__ import division

a = input('Digite o coeficiente angular da equação:')
b = input('Digite o coeficiente linear da equação:')
c = input('Digite o termo independente:')

delta = (b**2)-(4*a*c)

if (delta <0):
    print('A função não possui raízes reais!')
    
else:
    x1 = (-b+(delta**0.5))/(2*a)
    x2 = (-b-(delta**0.5))/(2*a)
    print ('%.2f' %x1)
    print ('%.2f' %x2)


