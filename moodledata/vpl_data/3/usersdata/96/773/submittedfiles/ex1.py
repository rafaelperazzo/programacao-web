# -*- coding: utf-8 -*-
from __future__ import division

a = input('Digite o valor de a:')
b = input('Digite o valor de b:')
c = input('Digite o valor de c:')
delta = b**2 - 4*a*c 

if delta < 0:
   print('Não possui raízes reais')
else:
     x1 = -b + (b**2 - 4*a*c)**0.5
     x2 = -b + (b**2 - 4*a*c)**0.5
     print('%.2f' %x1)
     print('%.2f' %x2)
