# -*- coding: utf-8 -*-
x1=float(input('digite x1:'))
x2=float(input('digite x2:'))
x3=float(input('digite x3:'))
x4=float(input('digite x4:'))
if x1>x2 and x1>x3 and x1>x4:
    print('%.f'%x1)
elif x2>x1 and x2>x3 and x2>x4:
    print('%.f'%x2)
elif x3>x1 and x3>x2 and x3>x4:
    print('%.f'%x3)
elif x4>x1 and x4>x2 and x4>x3:
    print('%.f'%x4)
if x1<x2 and x1<x3 and x1<x4:
    print('%.f'%x1)
elif x2<x1 and x2<x3 and x2<x4:
    print('%.f'%x2)
elif x3<x1 and x3<x2 and x3<x4:
    print('%.f'%x3)
else:
    print('%.f'%x4)
    