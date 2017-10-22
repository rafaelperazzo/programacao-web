# -*- coding: utf-8 -*-
import math
a=int(input('digite um numero: '))
b=int(input('digite um numero: '))
c=int(input('digite um numero: '))
d=int(input('digite um numero: '))
if (a==b==c==d) or (c>b and a>b and c<d):
    print('n')
else:
    while(c>b and c>d) or (b>c and b>a)   :
        print('s')
        break
    