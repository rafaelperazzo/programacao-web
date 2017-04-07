# -*- coding: utf-8 -*-
from __future__ import division
a =int(input('Digite a: '))
b =int(input('Digite b: '))
c =int(input('Digite c: '))
#COMECE A PARTIR DAQUI!
Delta=(b*b)-(4*(a)*(c))
x1=((-b)+(Delta**(0.5)))/(2*a)
x2=((-b)-(Delta**(0.5)))/(2*a)
if Delta >=0:
    print('O valor de x1 é: %.f' %x1)
    print('O valor de x2 é: %.f' %x2)
else:
    print('SRR')