# -*- coding: utf-8 -*-
import math
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
d=int(input('Digite d: '))

if a>b and b>c and c>d:
    print('S')
    
else:
    print('N')
    if c>a and c>b and c>d:
        print('S')
    
else:
    print('N')
    if d>a and d>b and d>c:
        print('S')
    else:
        print('N')
    
