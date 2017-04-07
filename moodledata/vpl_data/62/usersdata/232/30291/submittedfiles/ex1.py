# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
Equação=(a*(x**2))+(b*x)+(c)
Delta=((b)**2)-(4*a*c)
x1=((-b)+(Delta**(0.5)))/(2*a)
x2=((-b)-(Delta**(0.5)))/(2*a)
if Delta >=0:
    print('O valor de x1 é: %.5f'%x1)
    print('O valor de x2 é: %.5f'%x2)