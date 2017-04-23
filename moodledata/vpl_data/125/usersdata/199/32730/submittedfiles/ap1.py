# -*- coding: utf-8 -*-
a= float(input('Digite o Valor de A'))
b= float(input('Digite o Valor de B'))
c= float(input('Digite o Valor de C'))
if a<b and b<c:
    print('a')
    print('b')
    print('c')
elif a<c and c<b:
    print('a')
    print('c')
    print('b')
elif b<a and c<a:
    print('b')
    print('a')
    print('c')
elif c<a and c<b:
    print('c')
    print('a')
    print('b')
else:
    print('a')
    print('b')
    print('c')