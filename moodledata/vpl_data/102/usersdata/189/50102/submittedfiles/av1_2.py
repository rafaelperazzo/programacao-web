# -*- coding: utf-8 -*-
import math
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
d=int(input('digite o valor de d:'))
if a!=b and a==c and a!=d:
    print('V')
if b!=a and b!=c and b==d:
    print('V')
if a==c and a!=b and a!=d:
    print('V')
if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
    print('v')