# -*- coding: utf-8 -*-
from __future__ import division
print(' a*x**2+b*x+c ')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
delta=(b**2)-(4*a*c)
if delta>=0:
    x1=((-b) + (delta**0.5))/(2*a)
    x2=((-b) - (delta**0.5))/(2*a)
    print(x1)
    print(x2)
else:
    print('Não existem135 raízes reais.')