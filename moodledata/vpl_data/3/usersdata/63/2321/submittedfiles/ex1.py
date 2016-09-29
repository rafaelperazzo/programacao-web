# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')

delta=(b**2)-(4*a*c)



if delta>=0: 
    x1=((-b)+((delta)**(1/2.0)))/(2.0*a)
    x2=((-b)-((delta)**(1/2.0)))/(2.0*a)
    print('o valor de x1 =%.2f:' %x1)
    print('o valor de x2 =%.2f:' %x2)
    #print('mostrar x1 e x2')
elif delta<0:
    print('SRR')


