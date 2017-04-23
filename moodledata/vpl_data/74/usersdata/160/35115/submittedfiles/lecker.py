# -*- coding: utf-8 -*-
import math
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
d=int(input('Digite d: '))

if a>b and b>c and c>d:
    print('S')
    
elif a<b and b<c and c<d:
    print('N')
    
elif c>a and a<c and c<d:
    print('S')
    
elif d>a and a<b and d<c:
    print('S')
    
else:
    print('N')
    
