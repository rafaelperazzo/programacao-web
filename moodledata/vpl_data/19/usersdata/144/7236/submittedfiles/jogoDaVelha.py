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

if x1 == x2 == x3:
    print str(x1)
elif x4 == x5 == x6:
    print str(x4)
elif x7 == x8 == x9:
    print str(x7)
elif x1 == x4 == x7:
    print str(x1)
elif x2 == x5 == x8:
    print str(x2)
elif x3 == x6 == x9:
    print str(x3)
elif x1 == x5 == x9:
    print str(x1)
elif x3 == x5 == x7:
    print str(x4)

else:
    print "'E'"

