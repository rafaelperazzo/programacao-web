# -*- coding: utf-8 -*-
import math
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
d=int(input('Digite d: '))

if a>b and b>c and c>d:
    print('S')
    
elif a<b and b<c and c<d:
    print('S')
    if b>a and c>d and a<d:
        print('S')

elif c>a and a>b and b>d:
    print('S')
 
elif c<a and a<b and b<d:
    print('N')
    if d>a and a>b and b<d:
        print('N')
    if d<a and a<b and b<d:
        print('S')
    
else: 
    print('N')
