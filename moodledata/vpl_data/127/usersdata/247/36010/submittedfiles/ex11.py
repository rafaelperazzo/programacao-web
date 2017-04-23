# -*- coding: utf-8 -*-
a1=int(input('digite o ano da primeira data'))
m1=int(input('digite o mês da primeira data'))
d1=int(input('digite o dia da primeira data'))
a2=int(input('digite o ano da segunda data'))
m2=int(input('digite o mês da segunda data'))
d2=int(input('digite o dia da segunda data'))
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