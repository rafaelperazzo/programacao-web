# -*- coding: utf-8 -*-
from __future__ import division

a = input('digite o valor de a:')
b = input('digite o valor de b:')
c = input('digite o valor de c:')

delta = (b**2)-(4*a*c)

if delta >0:
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)
    print(x1)
    print(x2)
if delta ==0:
    x1 = (-b+delta**0.5)/(2*a)
    x2 = x1
    print('valor real de x1'%x1)
    print('valor real de x2'%x2)
if delta <0:
    print('não possui raízes reais')




a = input('digite o valaor de a:')
if a<0:
    r = a**2
    print('%.2f' % r)
if a>=0:
    r = a**0.5
    print('%.2f' % r)

    