# -*- coding: utf-8 -*-
from __future__ import division
a = input ('Digite o valor de a')
b = input ('Digite o valor de b')
a = input ('Digite o valor de c')

d = (b*b)-4*(a*c)

if d<0:
    input ('A equação não possui raízes reais')
else d>=0:
    x1 = (-b+(d**0.5))/(2*a) 
    x2 = (-b-(d**0.5))/(2*a) 
print ('As raízes da equação são: %.2f e %.2f' %x1 %x2)
    

