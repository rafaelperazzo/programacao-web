# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite o valor de a:')
b = input('Digite o valor de b:')
c = input('Digite o valor de c:')
D = ((b**2)-(4*a*c))

if D<0:
    print('Não existem raízes reais!')
    
else:
    x1 = -b+(D**(1/2))/(2*a)
    x2 = -b-(D**(1/2))/(2*a)
    print ('%.2f'%x1)
    print ('%.2f'%x2)
