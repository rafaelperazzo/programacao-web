# -*- coding: utf-8 -*-
from __future__ import division

a= input('Digite o valor de a: ')
b= input('Digite o valor de b: ')
c= input('digite o valor de c: ')

d= (b**2)-(4*a*c)
if d>=0:
    x1= ((-b)+(d**0.5))/(2*a)
    x2= ((-b)-(d**0.5))/(2*a)
    print x1
    print x2
else:
    print('Não há raízes reais.')
