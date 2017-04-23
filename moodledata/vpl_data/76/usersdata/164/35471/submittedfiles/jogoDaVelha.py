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
if (x1==x2==x3) and (x1==1):
    print('1')
elif (x1==x2==x3) and (x1==0):
    print('0')
elif (x4==x5==x6) and (x4==1):
    print('1')
elif (x4==x5==x6) and (x4==0):
    print('0')
elif (x7==x8==x9) and (x7==1):
    print('1')
elif (x7==x8==x9) and (x7==0):
    print('0')
elif (x1==x4==x7) and (x1==1):
    print('1')
elif (x1==x4==x7) and (x1==0):
    print('0')    
elif (x2==x5==x8) and (x2==1):
    print('1')
elif (x2==x5==x8) and (x2==0):
    print('0')
elif (x3==x6==x7) and (x3==1):
    print('1')
elif (x3==x6==x9) and (x3==0):
    print('0')
elif (x1==x5==x9) and (x1==1):
    print('1')
elif (x1==x5==x9) and (x5==0):
    print('0')
elif (x3==x5==x7) and (x3==1):
    print('1')
elif (x3==x5==x7) and (x3==0):
    print('0')
else:
    print('E')