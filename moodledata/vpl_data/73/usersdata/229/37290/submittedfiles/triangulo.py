# -*- coding: utf-8 -*-
import math

a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))

a>=b>=c>0

if(a<b+c):
    print('S')
else:
    print('N')
if(a<b+c):
    if(a**2)==(b**2)+(c**2):
        print('RE')
    if(a**2)>(b**2)+(c**2):
        print('OB')
    if(a**2)<(b**2)+(c**2):
        print('AC')
    if(a==b==c):
        print('EQ')
    if(b==c!=a):
        print('IS')
    if(a!=b) and (b!=c):
        print('ES')
    