# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')

d=(b**2)-4*a*c

x1=(-b+d**(1/2))/(2*a)
x2=(-b-d**(1/2))/(2*a)

if d<0:
    print('A Equação não possui raizes reais.")
    
else:
    print('x1= %.2f e x2= %.2f' %(x1,x2))