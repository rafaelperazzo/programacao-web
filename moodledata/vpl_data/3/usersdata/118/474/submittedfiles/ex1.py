# -*- coding: utf-8 -*-
from __future__ import division

#1
a = input('digite o valor de a = ')
b = input('digite o valor de b = ')
c = input('digite o valor de c = ')

#2
delta = (b**2)-(4*a*c)

if delta >=0 :
    x1 = ((-b) + (delta**0.5))/ 2*a
    x2 = ((-b) - (delta**0.5))/ 2*a
    print ('x1 = %.2f e x2 = %.2f') %(x1,x2)
    
else :
    print('Não possui raízes reais')

