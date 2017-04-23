# -*- coding: utf-8 -*-
import math

x1 = int(input('Digite x1: '))
x2 = int(input('Digite x2: '))
x3 = int(input('Digite x3: '))
x4 = int(input('Digite x4: '))
x5 = int(input('Digite x5: '))
x6 = int(input('Digite x6: '))
x7 = int(input('Digite x7: '))
x8 = int(input('Digite x8: '))
x9 = int(input('Digite x9: '))

#CONTINUE...

if x1==x2==x3:
    print(x1)
    
elif x4==x5==x6:
    print(x6)
    
elif x7==x8==x9:
    print(x7)
    
elif x1==x4==x7:
    print(x4)
    
elif x2==x5==x8:
    print(x2)
    
elif x3==x6==x9:
    print(x3)
    
elif x3==x5==x7:
    print(x5)
    
elif x1==x5==x9:
    print(x9)
    
else:
    print('E')