# -*- coding: utf-8 -*-
import math
a=float(input('Digite V1:'))
b=float(input('Digite V2:'))
c=float(input('Digite V3:'))
d=float(input('Digite V4:'))
if (b>a) and (b>c) or (c>b) and (c>d):
    print('S')
elif (c<b) and (c>d) and (b>=a):
    print('S')
elif (d>c) and (c>=b) and (b>=a):
    print('S')
else:
    print('N')
    