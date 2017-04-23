# -*- coding: utf-8 -*-
import math
a=float(input('Digite V1:'))
b=float(input('Digite V2:'))
c=float(input('Digite V3:'))
d=float(input('Digite V4:'))
if (a<b) and (b>c) and (c>d):
    print('S')
elif (a<b) and (b<c) and (c>d):
    print('S')
elif (a>b) and (c>=c) and (c>=d):
    print('S')
elif (a<=b) and (b<=c) and (c<d):
    print('S')
else:
    print('N')
    