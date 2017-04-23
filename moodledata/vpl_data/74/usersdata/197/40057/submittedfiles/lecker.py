# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor do número a:'))
b=int(input('Digite o valor do número b:'))
c=int(input('Digite o valor do número c:'))
d=int(input('Digite o valor do número d:'))
if a>b:
    if b>c and c>d:
        print('S')
    else:
        print('N')
if b>a and b>c:
    if d<c:
        print('S')
    else:
        print('N')
if c>d and c>b:
    if a<b:
        print('S')
    else:
        print('N')
if a==b==c==d:
    print('N')