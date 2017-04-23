# -*- coding: utf-8 -*-
d1=int(input('digite o dia da pessoa1:'))
m1=int(input('digite o mês da pessoa1:'))
a1=int(input('digite o ano da pessoa1:'))
d2=int(input('digite o dia da pessoa2:'))
m2=int(input('digite o mês da pessoa2:'))
a2=int(input('digite o ano da pessoa2:'))
if a1>a2:
    print('data da pessoa 1')
elif a1<a2:
    print('data da pessoa 2')
else:
    if m1>m2:
        print('pessoa 1')
    elif m1<m2: 
        print('pessoa 2')
    else:
        if d1>d2:
            print('pessoa 1')
        elif d1<d2:
            print('pessoa2')
        else:
            print('pessoas iguais')
            
        