# -*- coding: utf-8 -*-
from __future__ import divisio
a=input('digite um número')
b=input('digite um número')
c=input('digite um número')
RA=((b**2)-4*a*c)**(1/2)
if RA>0:
X1=-b+(RA)**(1/2)/2*a
print('resultado%.2f'%X1)
X2=-b-(RA)**(1/2)/2*a
print('resultado%.2f'%X2)
else
print('Não possui raízes reais')