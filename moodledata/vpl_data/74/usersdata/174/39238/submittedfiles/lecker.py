# -*- coding: utf-8 -*-
import math
a = float(input('Digite a:'))
b = float(input('Digite b:'))
c = float(input('Digite c:'))
d = float(input('Digite d:'))

if a<=b and b<=c and c<d:
    print ('S')
elif a<b and b>c and c<=d and d<b:
    print ('S')
elif a<=b and b<c and c>d:
    print ('S')
elif a>b and b<=c and c<=d:
    print ('S')
else:
    print ('N')