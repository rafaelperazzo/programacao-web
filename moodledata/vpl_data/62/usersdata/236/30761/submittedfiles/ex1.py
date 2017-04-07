# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
 
DELTA= (b*b)-(4*a*c)

if DELTA>=0:
    x1= (-b+ (DELTA)**1/2)/(2*a)
    x2= (-b- (DELTA)**1/2)/(2*a)
    print ('%f%f'%(x1,x2))
else:
    print ('SRR')
    