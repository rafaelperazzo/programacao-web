# -*- coding: utf-8 -*-
a=int(input('Digite o valor a: '))
b=int(input('Digite o valor b: '))
c=int(input('Digite o valor c: '))
d=int(input('Digite o valor d: '))
if a==b==c==d:
    print('N')
if a<b<c<d:
    print('S')
if a<b>c<d:
    print('N')
if a<b>c>d:
    print('S')
if a==b<c and d==a:
    print('S')
