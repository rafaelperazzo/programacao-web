# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('digite b: ')
c = input('digite c: ')
#COMECE A PARTIR DAQUI!


Delta = (b**2)-(4*a*c)

if Delta >= 0:
    x1=(-b)+(Delta**(1/2.0))/(2*a)
    x2=(-b)-(Delta**(1/2.0))/(2*a)
    print("as raizes sao: ")
    print('x1 %d: ' % x1)
    print('x2 %d: ' % x2)
    
else:
    print("SRR")
    
    

        