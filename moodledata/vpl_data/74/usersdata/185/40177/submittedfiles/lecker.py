# -*- coding: utf-8 -*-
import math
n1=int(input('digite n1:'))
n2=int(input('digite n2:'))
n3=int(input('digite n3:'))
if n1>n2 and n1>n3 and n1>n4:
    print('S')
elif n2>n1 and n2>n3 and n2>n4:
    print('S')
else:
    if n3>n1 and n3>n2 and n3>n4:
        print('S')
    elif n4>n1 and n4>n2 and n4>n3:
        print('S')
    else:
        print('N')