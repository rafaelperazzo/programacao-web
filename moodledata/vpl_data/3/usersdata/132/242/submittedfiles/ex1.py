# -*- coding: utf-8 -*-
from __future__ import division
a= input(' digite o valor de a: ')
b= input(' digite o valor de b: ')
c= input(' digite o valor de c: ')
w= (b**2)-(4*a*c)
x1= (-b+(w**0.5))/2*a
x2= (-b-(w**0.5))/2*a
if w<0:
    print(' a equacao nao possui raizes reais')
else:
    print(x1, x2)