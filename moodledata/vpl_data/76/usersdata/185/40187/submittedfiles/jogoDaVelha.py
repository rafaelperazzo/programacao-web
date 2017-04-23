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
if x1==0 and x2==0 and x3==0:
    print('0')
elif x4==0 and x5==0 and x6==0:
    print('0')
elif x7==0 and x8==0 and x9==0:
    print('0')
else:
    if x1==0 and x4==0 and x7==0:
        print('0')
    elif x2==0 and x5==0 and x8==0:
        print('0')
    elif x3==0 and x6==0 and x9==0:
        print('0')
    else:
        if x1==0 and x5==0 and x9==0:
            print('0')

