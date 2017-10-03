# -*- coding: utf-8 -*-
from __future__ import division
#COMECE A PARTIR DAQUI!
#ENTRADA
a= int(input(' digitar valor para a: '))
b= int(input(' digitar valor para b: '))
c= int(input(' digitar valor para c: '))

#PROCESSAMENTO
delta= (b**2)-4*a*c
x1= -b+ (delta**(1/2))/2*a
x2= -b- (delta**(1/2))/2*a

if(delta==0):
    print('%.2f' %x1)
    print('%.2f' %x2)
else:
    if(delta>0):
        print('%.2f' %x1)
    print('%.2f' %x2)
else: 
    if(delta<0):
        print('SRR')





