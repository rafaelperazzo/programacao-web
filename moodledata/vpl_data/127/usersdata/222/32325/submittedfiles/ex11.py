# -*- coding: utf-8 -*-
d1=int(input('Digite dia1:')
m1=int(input('Digite mes1:')
a1=int(input('Digite ano1:')
d2=int(input('Digite dia2:')
m1=int(input('Digite mes1:')
a1=int(input('Digite ano1:')
if a1>a2:
    print('%d/%d/%d'% (d1,m1,a1))
elif a1<a2:
    print('data 2')
else:
    if m1>m2:
        print('data 1')
    elif m1<m2:
        print('data 2')
    else:
        if d1>d2:
            print('data 1')
        elif d1<d2:
            print('data 2')
        else:
            print('iguais')
    
        