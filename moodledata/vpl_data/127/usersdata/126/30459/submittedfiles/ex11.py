# -*- coding: utf-8 -*-

a1= int(input('digite o ano da Data1:'))
a2= int(input('digite o ano da Data2:'))
m1= int(input('digite o mes da Data1:'))
m2= int(input('digite o mes da Data2:'))
d1= int(input('digite o dia da Data1:'))
d2= int(input('digite o dia da Data2:'))

if a1>a2:
    print('Data1')
else:
    if m1>m2:
        print('Data1')
    else:
        if a1>a2:
            print('Data1')
        else:
            if a1==a2 and m1==m2 and d1==d2:
                print('IGUAIS')
                
