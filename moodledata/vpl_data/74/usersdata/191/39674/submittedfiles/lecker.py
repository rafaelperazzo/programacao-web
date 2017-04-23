# -*- coding: utf-8 -*-
import math
n1=int(input('digite n1:'))
n2=int(input('digite o n2:'))
n3=int(input('digite o n3:'))
n4=int(input('digite o n4:'))
if n1>n2 and n4<=n3:
    print('S')
elif n1<n2 and n2>n3 and n4<n3:
    print('S')
elif n1<=n2 and n2<n3 and n4<n3:
    print('S')
elif n1<=n2 and n2<=n3 and n4>n3:
    print('S')
else:
    print('N')
