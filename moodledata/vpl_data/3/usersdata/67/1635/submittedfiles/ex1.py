# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
z=(b**2)-(4*a*c)
y=float ((-b)-(z**0.5)/(2*a)) 
x=(-b)+(z**0.5)/(2*a) 
if z >= 0:
 print "As raizes sao:"
 print(x)
 print(y)
elif z < 0:
 print ("SRR")
 



