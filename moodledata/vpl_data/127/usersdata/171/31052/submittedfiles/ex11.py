# -*- coding: utf-8 -*-
d1=int(input('digite o dia 1:'))
m1=int(input('digite o mes 1:'))
a1=int(input('digite o ano 1:'))
d2=int(input('digite o dia 2:'))
m2=int(input('digite o mes 2:'))
a2=int(input('digite o ano 2:'))
if a2>a1:
    print('DATA2')
elif a1>a2:
    print('DATA1')
elif a2==a1:
    if m2>m1:
        print('DATA 2')
    elif m2<m1:
        print('DATA 1')
elif m2==m1:
    if d2>d1:
        print('DATA2')
    elif d2<d1:
        print('DATA')
else:
    print('DATAS IGUAIS')
        
        
