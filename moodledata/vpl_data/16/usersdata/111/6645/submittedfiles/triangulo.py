# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite o valor do primeiro lado: ')
b=input('Digite o valor do segundo lado: ')
c=input('Digite o valor do terceiro lado: ')

if (a>=b>=c):
    print 'S'
    elif ((a**2) == (b**2) + (c**2)):
        print 'RE'
    elif ((a**2) > (b**2) + (c**2)):
        print 'OB'
    elif ((a**2) < (b**2) + (c**2)):
        print 'AC'
    elif (a==b==c):
        print 'EQ'
    elif (b==c!=a):
        print 'IS'
    elif (a!=b!=c):
        print 'ES'
    
else:
    print 'N'
    
