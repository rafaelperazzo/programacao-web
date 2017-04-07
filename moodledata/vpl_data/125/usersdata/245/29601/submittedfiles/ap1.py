# -*- coding: utf-8 -*-
a=float(input('Digite o valor de a:'))
b=float(input('Digite o valor de b:'))
c=float(input('Digite o valor de c:'))
if a>=b and a>=c:
    if b>=c:
        print(c)
        print(b)
        print(a)
    else:
        print(b)
        print(c)
        print(a)
elif b>=a and b>=c:
    if a>=c:
        print(c)
        print(a)
        print(b)
    else:
        print(a)
        print(c)
        print(b)
else:
    if a>=b:
        print(b)
        print(a)
        print(c)
    else:
        print(a)
        print(b)
        print(c)