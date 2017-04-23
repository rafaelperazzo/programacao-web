# -*- coding: utf-8 -*-
import math
x1=float(input('dig o x1:'))
x2=float(input('dig o x2:'))
x3=float(input('dig o x3:'))
x4=float(input('dig o x4:'))

if x1>x2 and x1>x3 and x1>x4:  
    print('S')
elif x2>x1 and x2>x3 and x2>x4:
    print('S')
elif x3>x1 and x3>x2 and x3>x4:
    print('S')
elif x4>x1 and x4>x2 and x4>x3:
    print('S')
else:
    print('N')
    
    
if x1>x2 and x1>x4 and x3>x2 and x3>x4:
    print('S')
elif x2>x1 and x2>x3 and x4>x3 and x4>x1:
    print('S')
elif x1>x2 and x1<x4 and x3>x2 and x3<x4:
    print('N')

elif x1==x2==x3==x4:
    print('N')
    
    
 