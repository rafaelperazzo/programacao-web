# -*- coding: utf-8 -*-
import math
a=int(input('Digite a variável 1: '))
b=int(input('Digite a variável 2: '))
c=int(input('Digite a variável 3: '))
d=int(input('Digite a variável 4: '))
if (b>a) and (b>c) and (d>c):
    print('N')
elif (c>d) and (c>b) and (a>b):
    print('N')
elif (b>a) and (b>c) or (c>b) and (c>d):
    print('S')
elif (a>b) and (d>c):
    print('N')
elif (a>b) or (dc):
    print('S')
else:
    print('N')
