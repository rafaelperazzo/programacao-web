# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
a=float(input('Digite o valor de a:'))
b=float(input('Digite o valor de b'))
c=float(input('Digite o valor de c'))
Delta=(b**2)-(4*a*c)
if Delta >=0:
   x1=(-b+Delta**1/2)/(2*a)
   x2=(-b-Delta**1/2)/(2*a)
   print('O valor da primeira raíz é: %f' %x1)
   print('O valor da segunda raíz é: %f' %x2)
else:
    print('SRR')