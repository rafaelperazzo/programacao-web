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

if x1==x2==x3 or x1==x4==x7 or x1==x5==x9:
    print('x1')
if x2==x5==x8 or x2==x1==x3:
    print('x2')
if x3==x2==x1 or x3==x5==x7 or x3==x6==x9:
    print('x3')
if x4==x5==x6 or x4==x1==x7:
    print('x4')

if x5==x2==x8 or x5==x4==x6 or x5==x1==x9:
    print('x5')

if x6==x2==x1 or x3==x3==x9:
    print('x6')

if x7==x4==x1 or x7==x5==x3 or x7==x8==x9:
    print('x7')

if x8==x5==x2 or x8==x7==x9:
    print('x8')

if x9==x5==x1 or x9==x6==x3 or x9==x7==x8:
    print('x9')

    

