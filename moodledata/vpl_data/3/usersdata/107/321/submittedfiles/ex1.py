# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')

d=(b**2)-(4*a*c)
if d>=0:
  x1=((-b)+(d**1/2))/2*a
  x2=((-b)-(d**1/2))/2*a
  print x1('%.2f' %x1)
  print x2('%.2f' %x2)
 else:
     print('não existe raízes reais:')
    
     
  