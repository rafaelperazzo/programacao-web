# -*- coding: utf-8 -*-
import math
a=float(input('Digite a: '))
b=float(input('Digite b: '))
c=float(input('Digite c: '))
d=float(input('Digite d: '))
if (a>b) and (b>=c) and (c>=d):
    print('S')
elif (b>a) and (b>c) and (c>=d):
    print('S')
elif (c>b) and (c>d) and (b>=a):
    print('S')
elif (d>c) and (c>=b) and (b>=a):
    print ('S')
else:
    print('N')