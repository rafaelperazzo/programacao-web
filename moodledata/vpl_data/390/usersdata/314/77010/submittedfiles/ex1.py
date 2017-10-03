# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta = b**2-4*a*c
if delta>0 :
    x1=(-b+delta**(0.5)) / 2*a
    x2=(-b-delta**(0.5)) /2*a
    print('x1 e x2 eh :{} {}'.format(x1,x2)  )
if delta==0 :
    x1=(-b+delta**(0.5)) / 2*a
    print('x eh :{}'.format(x1))
    