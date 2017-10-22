# -*- coding: utf-8 -*-
import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a>b and a>c and a>d or b>a and b>c and b>d or c>a and c>b and c>d or d>a and d>b and d>c:
    print('S')
else:
    print('N')