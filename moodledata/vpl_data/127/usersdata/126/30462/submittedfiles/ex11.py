# -*- coding: utf-8 -*-

a1= int(input('digite o ano da Data1:'))
a2= int(input('digite o ano da Data2:'))
m1= int(input('digite o mes da Data1:'))
m2= int(input('digite o mes da Data2:'))
d1= int(input('digite o dia da Data1:'))
d2= int(input('digite o dia da Data2:'))

if a1>a2:
    print('DATA1')
elif a2>a1:
    print('DATA2')
else:
    if m1>m2:
        print('DATA1')
    elif m2>m1:
        print('DATA2')
    else:
        if d1>d2:
            print('DATA1')
        elif d2>d1:
            print('DATA2')
        else:
            print('IGUAIS')



                
