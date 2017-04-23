# -*- coding: utf-8 -*-
d1=int(input('Digite o dia número 1: '))
m1=int(input('Digite o mês número 1: '))
a1=int(input('Digite o ano número 1: '))
d2=int(input('Digite o dia número 2: '))
m2=int(input('Digite o mês número 2: '))
a2=int(input('Digite o ano número 2: '))
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
            print('DATA 1')
        elif d1<d2:
            print('DATA 2')
        else:
            print('IGUAIS')
