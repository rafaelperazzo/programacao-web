# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta= float  ((b**2)-(4*a*c))
raiz1=(-b)+(delta**0.5)/(2*a)
raiz2=(-b)-(delta**0.5)/(2*a)
if delta >= 0:
 print raiz1, raiz2, "As raizes sao:"

else: 
 print("SRR")



