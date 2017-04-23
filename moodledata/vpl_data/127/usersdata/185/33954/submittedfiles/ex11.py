# -*- coding: utf-8 -*-
a1=int(input('digite ano um:'))
a2=int(input('digite ano dois:'))
m1=int(input('digite mes um:'))
m2=int(input('digite mes dois:'))
d1=int(input('digite dia um:'))
d2=int(input('digite dia dois:'))
if a1>a2:
    print('DATA 1')
elif a1<a2:
    print('DATA 2')
else:
    if m1>m2:
        print('DATA 1')
    elif m1<m2:
        print('DATA 2')
    else:
        if d1>d2:
            print ('DATA 1')
        elif d1<d2:
            print('DATA 2')
        else:
            print('IGUAIS')