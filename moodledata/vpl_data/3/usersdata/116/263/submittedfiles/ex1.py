# -*- coding: utf-8 -*-
from __future__ import division
a = input ('insira o valor de a:')
b = input ('insira o valor de b:')
c = input ('insira o valor de c:')

delta = (b**2)-4*a*c

if delta<0:
    print ('não existe raízes reais para a equação')
else :
    x1= (-b+(delta**(1/2)))/2*a
    x2= (-b-(delta**(1/2)))/2*a
    print (x1)
    print (x2)