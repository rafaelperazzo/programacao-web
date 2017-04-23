# -*- coding: utf-8 -*-
import math
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if a!=b!=c!=d and a>(b+c+d) or b>(a+c+d) or c>(b+a+d) or d>(b+c+a):
    print('S')
if a==b and a>(c+d) or b>(c+d):
    print('s')
if a==c and a>(b+d) or c>(b+d):
    print('s')
if a==d and a>(b+c) or d>(b+c):
    print('s')
if b==c and b>(a+d) or c>(a+d):
    print('s')
if b==d and b>(c+a) or d>(a+c):
    print('s')
if d==c and (c>(b+a) or d>(b+a)):
    print('s')




