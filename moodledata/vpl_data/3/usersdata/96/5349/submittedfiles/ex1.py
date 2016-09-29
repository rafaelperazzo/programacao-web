# -*- coding: utf-8 -*-
from __future__ import division

a = input('Digite o valor de a:')
b = input('Digite o valor de b:')
c = input('Digite o valor de c:')

Delta = (b**2 - (4*a*c))
if Delta >= 0:
    x1 = (- b + Delta**(1/2))/(2*a)
    x2 = (- b - Delta**(1/2))/(2*a)
    print(x1)
    print(x2)
else:
    print('SRR')
    
    