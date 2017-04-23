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
    print('N')
