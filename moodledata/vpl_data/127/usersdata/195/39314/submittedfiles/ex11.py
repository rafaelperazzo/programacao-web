# -*- coding: utf-8 -*-
a1=int(input('ano1:'))
a2=int(input('ano2:'))
m1=int(input('mes1:'))
m2=int(input('mes2:'))
d1=int(input('dia1:'))
d2=int(input('dia2:'))
if a1<a2:
    print('data1')
elif a1<a2:
    print('data2')
else:
    if m1>m2:
        print('data2')
    elif m1<m2:
        print('data2')
    else:
        if d1>d2:
            print('data1')
        elif d1<d2:
            print('data2')
        else:
            print('iguais')
