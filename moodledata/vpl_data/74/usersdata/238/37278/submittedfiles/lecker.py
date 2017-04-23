# -*- coding: utf-8 -*-
import math
a=int(input('digite o valor de 1:'))
b=int(input('digite o valor de 2:'))
c=int(input('digite o valor de 3:'))
d=int(input('digite o valor de 4:'))
if b>a and b>c and d>c:
    print('n')
elif c>d and a>b and c>b:
    print('n')
elif b>a and b>c or c>b and c>d:
    print('s')
elif a>b and d>c:
    print('n')
elif a>b or d>c:
    print('s')
else:
    print('n')
    

