# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')


delta=(b**2)-(4*a*c)

x1=(-b+((delta)**(1/2.0)))/2.0*a
x2=(-b-((delta)**(1/2.0)))/2.0*a

if delta>=0:
    print('Mostrar x1 e x2')
elif delta<0:
    print('SRR')
print(' O valor de x1 eh=%f:' %x1)
print(' O valor de x2 eh=%f:' %x2)


