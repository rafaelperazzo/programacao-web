# -*- coding: utf-8 -*-
from __future__ import division
a = input('digite o valor de a:') 
b = input('digite o valor de b:')
c = input('digite o valor de c:') 
delta = (b**2)-(4*a*c)
if deta>=0 :
    x1 = (-b+(delta)**(1/2))/(2*a)
    x2 = (-b-(delta)**(1/2))/(2*a)
    print('%.2f' %x1)
    print('%.2f' %x2)
else delta < 0 :
    print('nao possui raizes reais')
 
