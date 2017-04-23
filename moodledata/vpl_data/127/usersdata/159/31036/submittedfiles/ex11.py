# -*- coding: utf-8 -*-
d1=int(input('Dia 1'))
m1=int(input('Mês 1'))
a1=int(input('Ano 1'))
d2=int(input('Dia 2'))
m2=int(input('Mês 2'))
a2=int(input('Ano 2'))
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
            print('Data 1')
        elif d1<d2:
            print('Data 2')
        else:
            print('Iguais')