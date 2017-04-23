# -*- coding: utf-8 -*-
import math
a=float(input('a:'))
b=float(input('b:'))
c=float(input('c:'))
d=float(input('d:'))
if (a>b and a>c and a>d) or (a<=b and a<c and a<=d) or (a<b and a<c and a<=d) or (a<b and a>=c and a>=d) or (a<=b or b<=c c<d):
    print('S')
else:
    print('N')
