# -*- coding: utf-8 -*-
from __future__ import division
import math
a = int(input ('insira o valor de a:')) 
b = int(input ('insira o valor de b:')) 
c = int(input ('insira o valor de c:')) 

if a>=b and b>=c and c>0:
    if a<b+c: 
        print ('S') 
        if (a^2)==(b^2)+(c^2):
            print ('Re') 
        if (a^2)>(b^2)+(c^2):
            print ('Ob')
        if (a^2)<(b^2)+(c^2): 
            print ('Ac') 
    if a=b and b=c:
            print ('Eq')
        if c=b and b!=a:
            print ('Is)
        if a!=b and b!=c and a!=c
            print ('Es')
    else:
        print ('N')