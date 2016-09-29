# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=(b**2)-4*a*c
if d<0:
    print('A equação não possue raízes reais.')
else:
    x1=(-b+d**(1/2))/(2*a)
    x2=(-b-d**(1/2))/(2*a)
    print('x1:%.2f'%x1)
    print('x2:%.2f'%x2)
    