# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=input('digite o valor de d:')

elif a>b and b>=c and c>=d:
    print('S')
elif a<b and b>c and c>=d:
    print('S')
elif a<=b and b<=c and c>d:
    print('S')
elif a<=b and b>=c and c<d:
    print('S')
elif a<b and b>c and c<d:
    print('N')
elif a>b and b>c and c<d:
    print('N')
elif a>b and b<c and c<d:
    print('N')
else:
    print('N')