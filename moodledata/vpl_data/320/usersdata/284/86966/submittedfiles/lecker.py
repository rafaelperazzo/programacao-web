# -*- coding: utf-8 -*-
import math
a=int(input('digite um numero:4 '))
b=int(input('digite um numero:7 '))
c=int(input('digite um numero:5 '))
d=int(input('digite um numero:3 '))
if (a==b==c==d) or (c>b and a>b and c>d) or (b>c and b>a and d>c) or (a>b and c>d) or (a>b and d>c) :
    print('n')
else:
    print('s')
    
    