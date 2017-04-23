# -*- coding: utf-8 -*-

d1= int(input('digite o dia da Data1:'))
m1= int(input('digite o mes da Data1:'))
a1= int(input('digite o ano da Data1:'))
d2= int(input('digite o dia da Data2:'))
m2= int(input('digite o mes da Data2:'))
a2= int(input('digite o ano da Data2:'))

if a1>a2:
    print('DATA 1')
elif a2>a1:
    print('DATA 2')
else:
    if m1>m2:
        print('DATA 1')
    elif m2>m1:
        print('DATA 2')
    else:
        if d1>d2:
            print('DATA 1')
        elif d2>d1:
            print('DATA 2')
        else:
            print('IGUAIS')



                
