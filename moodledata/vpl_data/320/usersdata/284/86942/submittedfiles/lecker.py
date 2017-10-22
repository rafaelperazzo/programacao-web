# -*- coding: utf-8 -*-
import math
a=int(input('digite um numero: '))
b=int(input('digite um numero: '))
c=int(input('digite um numero: '))
d=int(input('digite um numero: '))
if (a==b==c==d):
    print('n')
else:
    while(b>c and b>a) or (c>d and c>b):
        print('s')
        break
    