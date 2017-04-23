# -*- coding: utf-8 -*-
import math
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if a>b and b<c and c<d:
    print('S')
elif b>a and a<c and c<d:
    print('S')
elif c>a and a<b and b<d:
    print('S')
elif d>a and a<b and b<c:
    print('S')
else:
    print('N')
            
        
    
    