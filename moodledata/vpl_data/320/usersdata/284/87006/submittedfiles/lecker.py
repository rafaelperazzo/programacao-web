# -*- coding: utf-8 -*-
import math
a=int(input('digite um numero:1 '))
b=int(input('digite um numero:1 '))
c=int(input('digite um numero:1 '))
d=int(input('digite um numero:2 '))
if (a==b==c==d) or (c>b and a>b and c>d) or (b>c and b>a and d>c) or (a>b and c>d) or (a>b and d>c)  :
    print('n')
else:
    print('s')
if (a==b and a==c and not(c=d)):
    print('s')

    
    