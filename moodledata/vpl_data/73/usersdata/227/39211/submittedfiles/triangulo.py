# -*- coding: utf-8 -*-
import math
a=int(input('digite uma valor'))
b=int(input('digite uma valor'))
c=int(input('digite uma valor'))

if  a**2==b**2+c**2:
    a>=b>=c>0
    a<b+c
    print('S')
    print('RE')
if a==b==c:
    a>=b>=c>0
    a<b+c
    print('eq')
if a**2>b**2+c**2:
    a>=b>=c>0
    a<b+c
    print('S')
    print('Ob')
if a==b!=c:
    a>=b>=c>0
    a<b+c
    print('Is')
if a**2<b**2+c**2:
    a>=b>=c>0
    a<b+c
    print('S')
    print('Ac')
if a!=b!=c:
    a>=b>=c>0
    a<b+c
    print('S')
    print('Es')
else:
    print('N')