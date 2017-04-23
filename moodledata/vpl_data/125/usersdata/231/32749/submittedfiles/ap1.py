# -*- coding: utf-8 -*-
x1=float(input('digite x1:'))
x2=float(input('digite x3:'))
x3=float(input('digite x2:'))
if x1<x2 and x2<x3:
    print('%.f'%x1)
    print('%.f'%x2)
    print('%.f'%x3)
if x1<x3 and x3<x2:
     print('%.f'%x1)
     print('%.f'%x3)
     print('%.f'%x2)
elif x2<x1 and x1<x3:
    print('%.f'%x2)
    print('%.f'%x1)
    print('%.f'%x3)
elif x2<x3 and x3<x1:
    print('%.f'%x2)
    print('%.f'%x3)
    print('%.f'%x1)
elif x3<x1 and x1<x2:
    print('%.f'%x3)
    print('%.f'%x1)
    print('%.f'%x2)
else:
    print('d')
    
   
    