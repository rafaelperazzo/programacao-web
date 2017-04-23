# -*- coding: utf-8 -*-
a1=int(input('digite ano 1:'))
a2=int(input('digite ano 2:'))
m1=int(input('digite mês 1:'))
m2=int(input('digite mês 2:'))
d1=int(input('digite dia 1:'))
d2=int(input('digite dia 2:'))
if a1>a2:
    print('Data 1')
elif a2>a1:
    print('Data 2')
else:
    if m1>m2:
        print('Data 1')
    elif m2>m1:
        print ('Data 2')
    else:
        if d1>d2:
            print ('Data 1')
        elif d2>d1:
            print ('Data 2')
        else:
            print ('IGUAIS')