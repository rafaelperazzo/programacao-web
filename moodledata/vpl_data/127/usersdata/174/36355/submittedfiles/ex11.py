# -*- coding: utf-8 -*-
d1 = float(input('Dia:'))
m1 = float(input('Mes:'))
a1 = float(input('Ano:'))
d2 = float(input('Dia:'))
m2 = float(input('Mes:'))
a2 = float(input('Ano:'))
if a1>a2:
    print ('DATA 1')
elif a1<a2:
    print ('DATA 2')
else:
    if m1>m2:
        print('DATA 1')
    elif m1<m2:
        print('DATA 2')
    else:
        if d1>d2:
            print('DATA 1')
        elif d1<d2:
            print('DATA 2')
        else:
            print('IGUAIS')