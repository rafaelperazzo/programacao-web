# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
n = b**2
Delta = (n - ((4*a)*c))
print("Delta = " , Delta)
raizdelta = Delta**0.5
print("Raiz de Delta" , raizdelta)
x1 = ((-b + raizdelta)/(2*a))
print("x1 = " , x1)
x2 = ((-b - raizdelta)/(2*a))
print("x2 = " , x2)
print('x1= %f' %x1)
