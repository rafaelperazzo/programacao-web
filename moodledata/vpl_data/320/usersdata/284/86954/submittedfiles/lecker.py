# -*- coding: utf-8 -*-
import math
a=int(input('digite um numero: '))
b=int(input('digite um numero: '))
c=int(input('digite um numero: '))
d=int(input('digite um numero: '))
if (a==b==c==d) or (c>b and a>b and c<d) or (b>c and b>a and d>c) or (a>b and c>d) or (a>b and d>c) or (b>a and c>d) or (b>a and d>c) :
    print('n')
else:
    while(c>b and c>d) or (b>c and b>a) or (a>b) or (a<b) or (c>d) or (d>c):
        print('s')
        break
    