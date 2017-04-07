# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
a=float(input('Digite o coeficiente a:'))
b=float(input('Digite o coeficiente b:'))
c=float(input('Digite o coeficiente c:'))
DeltaH=((b**2)-4*a*c)
x1=(((-b)+(DeltaH)**(1/2))/2*a)
x2=(((-b)-(DeltaH)**(1/2))/2*a)
if DeltaH>=0:
    print('%.2f' %x1)
    print('%.2f' %x2)
else:
    SRR