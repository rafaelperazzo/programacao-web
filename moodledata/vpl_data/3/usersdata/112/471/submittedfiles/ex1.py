# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')
RA=((b**2)-4*a*c)
if RA>0:
    XA=-b+(RA)**(1/2)/2*a
    print('resultado da primeira raiz: %.2f'%XA)
    XB=-b-(RA)**(1/2)/2*a
    print('resultado da segunda raiz: %.2f'%XB)
else:
    print('Não possui raízes reais')