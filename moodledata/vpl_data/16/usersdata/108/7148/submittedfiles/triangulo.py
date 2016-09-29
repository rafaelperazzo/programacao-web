# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int( input ('Digite a:'))
b = int( input ('Digite b:'))
c = int( input ('Digite c:'))

if (a>=(b+c)):
    print ('N')
else:
    print ('S')
    
    if ((a**2)==((b**2)+(c**2))):
       print ('Re')
    if ((a**2)>((b**2)+(c**2))):
        print ('Ob')
    if ((a**2)<((b**2)+(c**2))):
        print ('Ac')
    
    if ((a==b) and (a==c)):
        print ('Eq')
    if ((b==c) and (c!=a)):
        print ('Is')
    if ((a!=b) and (a!=c) and (a!=c)):
        print ('Es')
        
    
        
