# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!

D = (b**2)-(4*a*c)
if D >= 0 and a != 0:
    x1 = (-b+(D**0.5))/(2*a)
    x2 = (-b-(D**0.5))/(2*a)
    print ('x1 = %.2f'%x1)
    print ('x2 = %.2f'%x2)
elif a == 0:
    print('Nao é equaçao do 2º')
else:
    print ('SRR')