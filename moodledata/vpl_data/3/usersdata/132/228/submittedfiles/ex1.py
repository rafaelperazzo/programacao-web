# -*- coding: utf-8 -*-
from __future__ import division
a= input(' digite o valor de a: ')
b= input(' digite o valor de b: ')
c= input(' digite o valor de c: ')
w= (b**2)-(4*a*c)
if w<0:
    print(' a equacao nao possui raizes reais')
elif w>0:
    print(' a equacao possui duas raizes reais e distintas')
else:
    print(' equacao possui duas raizes reais e iguais')