# -*- coding: utf-8 -*-
from __future__ import division

a = input('Digite o valor de a:')
b = input('Digite o valor de b:')
c = input('Digite o valor de c:')

d = (b**2)-4*a*c

if d>=0 :
    x1 = (-b+((d)**0.5)))/2*a
    x2 = (-b-((d)**0.5)))/2*a
    
    print('O valor das raizes da equação são: %.1f %.1f'% (x1,x2))
else :
    print('A função não possui raizes reais')