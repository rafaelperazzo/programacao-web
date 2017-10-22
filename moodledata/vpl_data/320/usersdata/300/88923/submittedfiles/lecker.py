# -*- coding: utf-8 -*-
import math
x1 = int(input('Digite um valor: '))
x2 = int(input('Digite um valor: '))
x3 = int(input('Digite um valor: '))
x4 = int(input('Digite um valor: '))
if x1 > x2 and x2 >= x3 and x3 >= x4:
    print('S')
elif x1 > x2 and x2 <= x3 and x3 == x4:
    print('S') 
elif x1 < x2 and x2 > x3 and x3 >= x4:
    print('S')
elif x1 <= x2 and x2 < x3 and x3 > x4:
    print('S')
elif x1 <= x2 and x2 <= x3 and x3 < x4:
    print('S')
elif x1 == x2 and x2 <= x3 and x3 < x4:
    print('S')
else:
    print('N')
    