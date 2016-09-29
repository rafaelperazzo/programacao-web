# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite o primeiro termo:')
b=input('Digite o segundo termo:')
c=input('Digite o terceiro termo:')

delta=(b**2)-(4*a*c)
if delta<0:
    print('A equação não possui raízes reais')
if delta>=0:
    x=((-b)+(delta**0.5))/(2*a)
    y=((-b)-(delta**0.5))/(2*a)
    print('%.2f'%x)
    print('%.2f'%y)

    