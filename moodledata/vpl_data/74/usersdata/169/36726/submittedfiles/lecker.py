# -*- coding: utf-8 -*-
import math
a=int(input('Digite V1:'))
b=int(input('Digite V2:'))
c=int(input('Digite V3:'))
d=int(input('Digite V4:'))
if (b>a) and (b>c) or (c>b) and (c>d):
    print('S')
elif (a>b) and (b>=c) and (c>=d):
    print('S')
elif (d>c) and (c>=d) and (b>=a):
    print('S')
else:
    print('N')
    