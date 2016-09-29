# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input(''))
b=int(input(''))
c=int(input(''))

if a<b+c and b<c+a and c<a+b:
    print('S')
    if (a**2)==((b**2)+(c**2)):
        print('Re')
        if a==b and b==c:
            print('Eq')
        if a==b and b!=c or a==c and c!=b or c==b and c!=a:
            print('Is')
        if a!=b and a!=c and b!=c:
            print('Es')
else:
    print ('N')
