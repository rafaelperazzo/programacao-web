# -*- coding: utf-8 -*-
import math
a=int(input(''))
b=int(input(''))    
c=int(input(''))
d=int(input(''))
if a<b and b<c and c>d:
    print('S')
elif a<b and b>c and c>d:
    print('S')
elif a>b and b>c and c>d:
    print('S')
elif a<b and b<c and c<d:
    print('S')
else:
    print('N')