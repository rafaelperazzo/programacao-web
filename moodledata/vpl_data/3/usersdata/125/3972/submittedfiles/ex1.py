# -*- coding: utf-8 -*-
from __future__ import division
import math
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!

delta=(b**2)-4*a*c



if delta >=0:
   x=math.sqrt(delta)
   x1=(-b+x)/(2*a)
   x2=(-b-x)/(2*a)
  
   print x1=a
   print x2=a

else:  
   print 'SRR'