# -*- coding: utf-8 -*-
a=float(input('digite o valor de a:'))
b=float(input('digite o valor de b:'))
c=float(input('digite o valor de c:'))
if a>b and b>c:
    print(a)
    print(b)
    print(c)
elif a>c and c>b:
    print(a)
    print(c)
    print(b)
elif b>a and a >c:
    print(b)
    print(a)
    print(c)
    
    