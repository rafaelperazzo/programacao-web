# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!

Delta=(b**2)-(4*a*b)
x1=((Delta**0.5)-b)/(2*a)
x2=((b+(Delta**0.5))-)/(2*a)

if Delta>=0:
   print ('%.2F e %.2f' %(x1,x2))
else:
    print SRR