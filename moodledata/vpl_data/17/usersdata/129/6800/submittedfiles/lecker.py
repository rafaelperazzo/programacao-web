# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor: ')
b=input('Digite o valor: ')
c=input('Digite o valor: ')
d=input('Digite o valor: ')
if a>b and b>=c and c>=d:
    print ('S')
elif  b>c and a<=b and c>=d:
    print ('S')
elif a<=b and b<=c and c<d:
    print ('S')
elif a<=b and b<=c and c<d:
    print ('S')
else :
    print ('N')
