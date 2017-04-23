# -*- coding: utf-8 -*-
a1=float(input('digite ano 1:'))
a2=float(input('digite ano 2:'))
m1=float(input('digite mes 1:'))
m2=float(input('digite mes 2:'))
d1=float(input('digite dia 1:'))
d2=float(input('digite dia 2:'))
if a1>a2:
    print('Data 1')
elif a1<a2:
    print('Data 2')
else:
    if m1>m2:
        print('Data 1')
    elif m1<m2:
        print('Data 2')
    else:
        if d1>d2:
            print ('Data 1')
        elif d1<d2:
            print('Data 2')
        else:
            print('iguais')