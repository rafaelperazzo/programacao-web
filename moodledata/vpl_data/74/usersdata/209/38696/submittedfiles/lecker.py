# -*- coding: utf-8 -*-
import math
a=int(input('A:'))
b=int(input('B:'))
c=int(input('C:'))
d=int(input('D:'))
if a>b and d<c and c<b:
    print('s')
elif a<b and b>c and d<c:
    print('s')
elif a<b and b<c and d<c:
    print('s')
elif a<b and b<c and d>c:
    print('s')
else:
    print('n')