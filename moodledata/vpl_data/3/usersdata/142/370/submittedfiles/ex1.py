# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')

delta = ((b**2)-4*a*c)

if delta>=0:
    x1 = ((-b)+((delta)**0.5))/2*a
    x2 = ((-b)-((delta)**0.5))/2*a
    print ('O valor da primeira raiz é: %.1f'% x1)
    print ('O valor da segunda raiz é: %.1f'% x2)
else:
    print ('Essa equação não possui raizes reais')
