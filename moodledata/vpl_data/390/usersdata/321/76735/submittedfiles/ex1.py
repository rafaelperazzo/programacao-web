# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA

a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')

#CALCULO DO DELTA

delta= b ** 2 - 4 * a * c

#TESTES

if delta<0 :
    print('SRR')
    
else :
    if delta>=0:
        x1=(- b + delta ** (1/2))/ 2 * a
        x2=(- b - delta ** (1/2))/ 2 * a
        print('X1=%.2f' % x1)
        print('X2=%.2f' % x2)