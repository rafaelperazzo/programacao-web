# -*- coding: utf-8 -*-
import math
a=int(input('digite a :'))
b=int(input('digte b:'))
c=int(input('digite c:'))
d=int(input('digite d:'))
if a!=b and a==c and a!=d:
    print('V')
if b!=a and b!=c and b==d:
    print ('V')
if c==a and c!=b and c!=d:
    print('V')
if d!=a and d==b and d!=c:
    print('V')
if a!=b and a!=c and a==d:
    print('F')
if b!=a and b==c and b!=d:
    print('F')
if c!=a and c!=b and c==d:
    print('F')
if a==b and a!=c and a!=d:
    print('F')
  
