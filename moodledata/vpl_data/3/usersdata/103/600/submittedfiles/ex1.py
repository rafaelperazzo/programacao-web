# -*- coding: utf-8 -*-
from __future__ import division

a=input('Seguindo a fórmula AX²+BX+C, insira o valor de A:')
b=input('Seguindo a fórmula AX²+BX+C, insira o valor de B:')
c=input('Seguindo a fórmula AX²+BX+C, insira o valor de C:')
d=(b**2)-(4*a*c)
if d>0:
    x1=(-b+(d**0.5))/(2*a)
    x2=(-b-(d**0.5))/(2*a)
    print('%.2f %.2f'%(x1,x2))
if d==0:
    x=-b/(2*a)
    print('%.2f'%x)
if (b**2)-(4*a*c)<0:
    print('A equação não possui raizes reais')
    