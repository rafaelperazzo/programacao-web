# -*- coding: utf-8 -*-
import math
a=float(input('digite um numero:'))
b=float(input('digite um numero:'))
c=float(input('digite um numero:'))
d=float(input('digite um numero:'))
if a!=b!=c!=d:
    if a<b>c:
        if c>d:
            print('S')
        else:    
            print('N')
    elif  b<c>d:  
        if a<b:
            print('S')
        else:
            print('N')
    elif a>b: 
        if c<b and d<b:
            print('S')
        else:
            print('N')
    elif d>c: 
        if a<c and b<c:
            print('S')
        else:
            print('N')
else:
    if a!=b and a!=c and a!=d:
        if a>b and b>=c and b>=d:
            print('S')
        else:
            print('n')
    elif b!=a and b!=c and b!=d:
        if a<b>c and d<=c:
            print('S')
        else:
            print('N')
    elif  c!=a and c!=b and c!=d:
        if b<c>d and a<=b:
            print('S')
        else:
            print('N')
    elif d!=a and d!=b and d!=c:
        if d>c and c>=b>=a:
            print('S')
        else:
            print('N')
    
