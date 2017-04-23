# -*- coding: utf-8 -*-
a1=int(input('digite a1:'))
a2=int(input('digite a2:'))
m1=int(input('digite m1:'))
m2=int(input('digite m2:'))
d1=int(input('digite d1:'))
d2=int(input('digite d2:'))
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
            print('IGUAIS')