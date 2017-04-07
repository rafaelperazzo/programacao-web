# -*- coding: utf-8 -*-
d1=int(input('Digite o dia:'))
m1=int(input('Digite o mes:'))
a1=int(input('Digite o ano:'))
d2=int(input('Digite o dia:'))
m2=int(input('Digite o mes:'))
a2=int(input('Digite o ano:'))
if a1>a2:
    print('Data 1')
if a1<a2:
    print('Data 2')
else:
    if m1>m2:
        print('Data 1')
    elif m1<m2:
        print('Data 2')
    else:
        if d1>d2:
            print('Data 1')
        elif d1<d2:
            print('Data 2')
        else:
            print('Iguais')


