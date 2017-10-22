# -*- coding: utf-8 -*-
import math
v1 = int(input('valor: '))
v2 = int(input('valor: '))
v3 = int(input('valor: '))
v4 = int(input('valor: '))
if v1 > v2 or v4 > v3:
    print('S')
elif v2 > v1 and v2 > v3:
    print('S')
elif v3 > v2 and v3 > v4: 
    print('S')
else:
    print('N')