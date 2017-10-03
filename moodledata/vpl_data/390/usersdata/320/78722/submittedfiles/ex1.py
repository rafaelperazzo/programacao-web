# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
delta = (b**2) - (4*a*c)
if delta >= 0:
    X1 = (-b + delta**(1/2))/(2*a)
    X2 = (-b - delta**(1/2))/(2*a)
    print ('%f' %X1)
    print ('%f' %X2)
else:
    print ('Sem raizes reais')