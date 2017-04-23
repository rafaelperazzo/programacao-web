# -*- coding: utf-8 -*-
import math
a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))
d=int(input('Digite d:'))

if a>b and b>c and c>d and b!=c!=d:
    print('S')
elif a<b>c and d<c and c!=d:
    print('S')
elif a<b and b<c>d and a!=b!=d:
    print('S')
elif a<b and b<c and d>c and b!=c!=a:
    print('S')
else:
    print('N')