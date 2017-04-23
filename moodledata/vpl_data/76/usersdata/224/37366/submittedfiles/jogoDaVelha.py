# -*- coding: utf-8 -*-
import math

x1 = int(input('Digite x1: '))
x2 = int(input('Digite x2: '))
x3 = int(input('Digite x3: '))
x4 = int(input('Digite x4: '))
x5 = int(input('Digite x5: '))
x6 = int(input('Digite x6: '))
x7 = int(input('Digite x7: '))
x8 = int(input('Digite x8: '))
x9 = int(input('Digite x9: '))

if x1==x2==x3 or x4==x5==x6 or x7==x8==x9:
    print(x1)
else:
    if x1==x4==x7 or x2==x5==x8 or x3==x6==x9:
        print(x9)
    else:
        if x1==x5==x9 or x3==x5==x7:
            print(x1)
        else:
            print('E')


