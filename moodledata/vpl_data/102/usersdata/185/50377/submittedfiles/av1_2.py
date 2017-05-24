# -*- coding: utf-8 -*-
import math
a=int(input('digite um numero de 0 a 9:'))
b=int(input('digite um numero de 0 a 9:'))
c=int(input('digite um numero de 0 a 9:'))
d=int(input('digite um numero de 0 a 9:'))
if a==c and b!=d:
    print('V')
elif b==d and a!c:
    print('V')
else:
    print('F')
        
    
