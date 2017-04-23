# -*- coding: utf-8 -*-
import math
a=int(input('digitite o valor 1:'))
b=int(input('digitite o valor 2:'))
c=int(input('digitite o valor 3:'))
d=int(input('digitite o valor 4:'))
if b>a and b>c or c>b and c>d:
    print('S')

if c>a and c>b or b>c and b>d:
    print('S')

if b>d and b>c or c>b and c>a:
    print('S')

if c>d and c>b or b>c and b>a:
    print('S')

if a>c and a>b or b>a and b>d:
    print('S')

if b>c and b>a or a>b and a>d:
    print('S')

if a>d and a>b or b>a and b>c:
    print('S')

if b>d and b>a or a>b and a>c:
    print('S')

else:
    print('N')
    