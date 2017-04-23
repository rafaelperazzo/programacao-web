# -*- coding: utf-8 -*-
import math
c=float(input('digite c:'))
d=float(input('digite d:'))
e=float(input('digite e:'))
f=float(input('digite f:'))
if d>=c and d>e and e<f:
    print('N')
elif e>=f and e>d and c>d:
    print('N')
elif d>=c and d>e and e>d and e>f:
    print('S')
elif c>=d and e>f:
    print('N')
elif c>=d and f>e:
    print('S') 
else:
    print('N')