# -*- coding: utf-8 -*-
from __future__ import division

a= input('Digite o valor de a: ')
b= input('Digite o valor de b: ')
c= input('Digite o valor de c: ')

delta= (b)**(2)+(-4*(a)*(c))


if delta<0:
    print('Esta equação não possui raízes reais')
else:
    x1= ((-b)+(delta)*(1/2))/2a
    x2= ((-b)-(delta)*(1/2))/2a
    print ('%.2f' %x1)
    print ('%.2f' %x2)