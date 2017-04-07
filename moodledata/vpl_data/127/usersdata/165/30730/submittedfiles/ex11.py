# -*- coding: utf-8 -*-
d1=int(input('digite o primeiro dia:'))
m1=int(input('digite o primeiro mes:'))
a1=int(input('digite o primeiro ano:'))
d2=int(input('digite o segundo dia:'))
m2=int(input('digite o segundo mes:'))
a2=int(input('digite o segundo ano:'))
if a2<a1:
    print('data 1')
elif a1<a2:
    print('data 2')
elif a1=a2 and m1!=m2:
    if m2<m1:
        print('data 1')
    else:
        print('data 2')
elif a1=a2 and m1=m2:
    if d2<d1:
        print('data 1')
    elif d1<d2:
        print('data 2')
    else:
        print('iguais')
        
