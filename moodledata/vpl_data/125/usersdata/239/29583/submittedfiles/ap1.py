# -*- coding: utf-8 -*-
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
if a>b and b>c:
    print(a)
    print(b)
    print(c)
elif b>a and a>c:
    print(b)
    print(a)
    print(c)
elif c>a and a>b:
    print(c)
    print(a)
    print(b)