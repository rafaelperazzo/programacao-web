# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!

z=(b**2)-(4*a*c)

if z >= 0:
    
    y=(((-b)-(z**(1/2.0)))/(2*a)) 
    x=(-b)+(z**0.5)/(2*a) 
    print "As raizes sao: "
    print(x)
    print(y)
 
else:
 print ("SRR")
 



