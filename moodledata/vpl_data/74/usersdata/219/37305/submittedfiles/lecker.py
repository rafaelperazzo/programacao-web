# -*- coding: utf-8 -*-
import math
a1=float(input('Digite a1:'))
a2=float(input('Digite a2:'))
a3=float(input('Digite a3:'))
a4=float(input('Digite a4:'))
if a1>a2>a3>a4:
    print('S')
elif a1<a2>a3>a4:
    print('S')
elif a1<a2<a3>a4:
    print('S')
elif a1<a2<a3<a4:
    print('s')
else:
    print('N')