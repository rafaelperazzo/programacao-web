# -*- coding: utf-8 -*-
from __future__ import division
import math
a =  int(input('Digite o valor de A:'))
b =  int(input('Digite o valor de B:'))
c =  int(input('Digite o valor de C:'))
d =  int(input('Digite o valor de D:'))
if a<=b and a<=c and a<=d:
    print 'S'
elif a>=b<=c<=d:
    print 'S'
elif a>=b>=c<=d:
    print 'S'
elif a>=b>=c>=d:
    print 'S'
else:
    print 'N'