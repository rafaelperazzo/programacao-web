# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!

Delta= a*(x*x)+(b*x)+c 

if Delta>=0:
    x1=(-b+(Delta)**(1/2))/(2*a)
    x2=(-b-(Delta)**(1/2))/(2*a)
    print ('%.2f' %x1)
    print ('%.2f' %x2)

else:
    print ("SRR")

