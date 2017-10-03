# -*- coding: utf-8 -*-
d1 = int(input('digite o dia: '))
m1 = int(input('digite o mes: '))
a1 = int(input('digite o ano: '))
d2 = int(input('digite o dia: '))
m2 = int(input('digite o mes: '))
a2 = int(input('digte o ano: '))
if a1<a2:
    print('DATA 2')
if (a1==a2) and (m1<m2):
    print('DATA 2')
if (a1==a2) and (m1==m2) and (d1<d2):
    print('DATA 2')
if a1>a2:
    print('DATA 1')
if (a1==a2) and (m1>m2):
    print('DATA 1')
if (a1==a2) and (m1==m2) and (d1>d2):
    print('DATA 1')
if (a1==a2) and (m1==m2) and (d1==d2):
    print('IGUAIS')