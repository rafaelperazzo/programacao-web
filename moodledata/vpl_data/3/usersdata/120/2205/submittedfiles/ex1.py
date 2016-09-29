# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite o valor de a:')
b = input('Digite o valor de b:')
c = input('Digite 0 valor de c:')
#PROCESSAMENTO
r=('(a*x**2)+(b*x)+c:')
delta=(b**2)-4*a*c
x1=((-b)+(delta**0.5))/(2*a)
x2=((-b)-(delta**0.5))/(2*a)
#SAIDA
if delta>=0:
   print('x1=%.2f'%x1)
   print('x2=%.2f'%x2)
else:
    print('SRR')
    
