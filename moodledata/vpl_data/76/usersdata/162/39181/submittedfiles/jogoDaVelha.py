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
if x1==x2==x3==1:
    print('1')
if x1==x4==x7==1:
    print('1')
if x2==x5==x8==1:
    print('1')
if x3==x6==x9==1:
    print('1')
if x4==x5==x6==1:
    print('1')
if x7==x8==x9==1:
    print('1')
if x1==x5==x9==1:
    print('1')
if x3==x5==x7==1:
    print('1')
if x1==x2==x3==0:
    print('0')
if x1==x4==x7==0:
    print('0')
if x2==x5==x8==0:
    print('0')
if x3==x6==x9==0:
    print('0')
if x4==x5==x6==0:
    print('0')
if x7==x8==x9==0:
    print('0')
if x1==x5==x9==0:
    print('0')
if x3==x5==x7==0:
    print('0')
if x1==x2!=x3 and x4==x5!=x6 and x8==x9!=x7 and x1==x7 and x5==x8 and x3==x9:
    print('E')

    

