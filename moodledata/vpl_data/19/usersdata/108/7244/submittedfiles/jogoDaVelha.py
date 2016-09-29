# -*- coding: utf-8 -*-
from __future__ import division
import math

x1 = input('Digite x1: ')
x2 = input('Digite x2: ')
x3 = input('Digite x3: ')
x4 = input('Digite x4: ')
x5 = input('Digite x5: ')
x6 = input('Digite x6: ')
x7 = input('Digite x7: ')
x8 = input('Digite x8: ')
x9 = input('Digite x9: ')

if ((x1==x2) and (x1==x3)):
    print (x1)
elif ((x4==x5) and (x4==x6)):
    print (x4)
elif ((x7==x8) and (x7==x9)):
    print (x7)
elif ((x1==x4) and (x1==x7)):
    print (x1)
elif ((x2==x5) and (x2==x8)):
    print (x2)
elif ((x3==x6) and (x3==x9)):
    print (x3)
elif ((x1==x5) and (x1==x9)):
    print (x1)
elif ((x3==x5) and (x3==x7)):
    print (x3)
else:
    print ('E')
