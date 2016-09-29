# -*- coding: utf-8 -*-
from __future__ import divisio
a=input('digite um número')
b=input('digite um número')
c=input('digite um número')
RA=((b**2)-4*a*c)
if RA>0:
    XA=-b+(RA)**(1/2)/2*a
    print('resultado%.2f'%XA)
    XB=-b-(RA)**(1/2)/2*a
    print('resultado%.2f'%XB)
else
    print('Não possui raízes reais')