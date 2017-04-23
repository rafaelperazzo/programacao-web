# -*- coding: utf-8 -*-
d1=int(input('Digite o dia da data 1:'))
m1=int(input('Digite o mês da data 1:'))
a1=int(input('Digite o ano da data 1:'))
d2=int(input('Digite o dia da data 2:'))
m2=int(input('Digite o mês da data 2:'))
a2=int(input('Digite o ano da data 2:'))
if  a1<a2:
    print('DATA 2')
else:
    print('DATA 1')
    if  a1==a2:
        if  m1>m2:
            print('DATA 1')
        else:
            print('DATA 2')