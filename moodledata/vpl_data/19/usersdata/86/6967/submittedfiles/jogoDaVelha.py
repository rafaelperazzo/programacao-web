# -*- coding: utf-8 -*-
from __future__ import division
import math

x1 = input('Digite x1: ')
x2 = input('Digite x2: ')
x3 = input('Digite x3: ')
x4 = input('Digite x4: ')
x5 = input('Digite x5: ')
x6 = input('Digite x6: ')
x7 = input('Digite x7: ')
x8 = input('Digite x8: ')
x9 = input('Digite x9: ')


if x1==x2==x3==1 or x4==x1==x7==1 or x1==x5==x9==1 or x4==x5==x6==1 or x7==x8==x9==1 or x7==x5==x3==1 or x2==x3==x8==1 or x3==x6==x9==1:
    print(1)
elif x1==x2==x3==0 or x4==x1==x7==0 or x1==x5==x9==0 or x4==x5==x6==0 or x7==x8==x9==0 or x7==x5==x3==0 or x2==x3==x8==0 or x3==x6==x9==0:
    print(0)
else:
    print('E')
    

