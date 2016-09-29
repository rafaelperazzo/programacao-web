# -*- coding: utf-8 -*-
from __future__ import division
a = input ('Digite o valor de a: ')
b = input (' Digite o valor de b: ')
c = input ('Digite o valor de c: ')

#processamento
delta =(b**2) - (4*a*c)

if delta>0:
    x1=(-b+(delta**0.5))/2*a
    x2= (-b-(delta**0.5))/2*a
    print(' %.2f' %x1)
    print('%.2f' %x2)
if delta==0:
    x1=-b/2*a
    x2= x1
    print ('%.2f' %x1)
    print ('%.2f' %x2)
if delta<0:
    print ('A equação não possui raízes reais')
#entrada
a = input ('Digite um valor para a:')

#processamento
if a>=0:
    b = a**0.5
    print ('%.2f' %b)
if a<0:
    b = a**2
    print ('%.2f' %b)
