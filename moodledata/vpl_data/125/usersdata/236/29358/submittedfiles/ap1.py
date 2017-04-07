# -*- coding: utf-8 -*-
a=float(input('Digite o primeiro número:'))
b=float(input('Digite o segundo número:'))
c=float(input('Digite o terceiro número:'))

if a>b>c:
    print(c)
    print(b)
    print(a)
elif b>a>c:
    print(c)
    print(a)
    print(b)
elif c>b>a:
    print(a)
    print(b)
    print(c)
elif c>a>b:
    print(b)
    print(a)
    print(c)
    