# -*- coding: utf-8 -*-
from __future__ import division
print ('Cálculo dos valores de x na equação: a*(x**2) + (b*x) + c')
a = input ('Digite o valor de a:')
b = input ('Digite o valor de b:')
c = input ('Digite o valor de c:')

d = (b*b)-4*(a*c)

if d<0:
    input ('A equação não possui raízes reais')
else:
    x1 = (-b+(d**0.5))/(2*a) 
    x2 = (-b-(d**0.5))/(2*a) 
print ("%.2f" %x1)
print ("%.2f" %x2)
    

