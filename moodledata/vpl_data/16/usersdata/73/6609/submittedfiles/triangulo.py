# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input ('digite o valor de a:')
b=input ('digite o valor de b:')
c=input ('digite o valor de c:')

if a<b+c:
    print ('s')
    if (a*a)==(b*b)+(c*c):
        print ('Re')
    if (a*a)>(b*b)+(c*c):
        print ('Ob')
    if (a*a)<(b*b)+(c*c): 
        print ('Ac')
    if a==b==c:
        print ('Eq')
    if b==c!=a:
        print ('Is')
    if a!=b!=c:
        print ('Es')
else:
    print ('N')