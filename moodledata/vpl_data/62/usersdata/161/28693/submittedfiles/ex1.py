# -*- coding: utf-8 -*-
from __future__ import division
a =float(input('Digite a: '))
b =float(input('Digite b: '))
c =float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
Delta=(b*b)-(4*a*c)
if Delta >=0:
   x1=(-b+Delta**1/2)/(2*a)
   x2=(-b-Delta**1/2)/(2*a)
   print('O valor da primeira raíz é: %f' %x1)
   print('O valor da segunda raíz é: %f' %x2)
else:
    print('SRR')