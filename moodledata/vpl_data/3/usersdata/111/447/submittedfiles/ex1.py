# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')
d=((b**2) - (4*a*c))
e=((-b) + (d**0.5))/(2*a)
f=((-b) - (d**0.5))/(2*a)
if d<0 : 
    print ('Não existem raízes reais ')
else :
    print e 
    print f