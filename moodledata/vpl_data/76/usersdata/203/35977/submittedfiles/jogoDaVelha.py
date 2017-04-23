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

#CONTINUE...
if x1==1:
    if (x1==x4 and x4==x7) or (x1==x5 and x5==x9) or (x1==x2 and x2==x3):
        print('1')
elif x1==0:
    if (x1==x4 and x4==x7) or (x1==x5 and x5==x9) or (x1==x2 and x2==x3):
        print('0')
elif x2==1:
    if (x2==x5 and x5==x8):
        print('1')
elif x2==0:
    if (x2==x5 and x5==x8):
        print('0')
elif x3==1:
    if (x3==x6 and x6==x9) or (x3==x5 and x5==x7):
        print('1')
elif x3==0:
    if (x3==x6 and x6==x9):
        print('0')
else:
    print('E')
        