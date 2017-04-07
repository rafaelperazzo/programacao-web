# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta= (b*b)-(4*(a*c))
x1= (-b+(delta**(1/2)))/2*a 
x2= (-b-(delta**(1/2)))/2*a
if delta >=0 :
    print ('x1=%.2f'%x1)
    print ('x2=%.2f'%x2)
else: 
    print('SRR')