# -*- coding: utf-8 -*-
import math
a=float(input('digite a: '))
b=float(input('digite b: '))
c=float(input('digite c: '))
d=float(input('digite d: '))

if a>b and c<b and c>d:
    print('S')
if b>a and b>c and c>d:
    print('S')
if c>b and c>d and b>a:
    print('S')
if d>c and c>b and b>a:
    print('S')
    
if (a>b and c<b and c>d) and (b>a and b>c and c>d) and (c>b and c>d and b>a) and (d>c and c>b and b>a) == not:
    print('N')