# -*- coding: utf-8 -*-
d1=int(input('digite o dia 1:'))
m1=int(input('digite o mes 1:'))
a1=int(input('digite o ano 1:'))
d2=int(input('digite o dia 2:'))
m2=int(input('digite o mes 2:'))
a2=int(input('digite o ano 2:'))
if a1>a2:
    print('DATA1')
elif a1<a2:
    print('DATA2')
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
            print('DATAS IGUAIS')

        
        
        
