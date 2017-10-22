# -*- coding: utf-8 -*-
import math
a=float(input("digite o numero:"))
b=float(input("digite o numero:"))
c=float(input("digite o numero:"))
d=float(input("digite o numero:"))
if a>b>c>d or a>b<c>d or a<b>c<d or a>b<c<d:
    print('n')
elif a>b:
    print('s')
elif b>a and b>c:
    print('s')
elif c>b and c>d:
    print('s')
elif d>c:
    print('s')
else:
    print('n')