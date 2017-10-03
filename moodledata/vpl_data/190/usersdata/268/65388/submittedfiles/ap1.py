# -*- coding: utf-8 -*-
a= float(input('Digite o primeiro numero: '))
b= float(input('Digite o segundo numero: '))
c= float(input('Digite o terceiro numero: '))

if (a>b) and (b>c):
    print(c)
    print(b)
    print(a)
elif (b>c) and (c>a):
    print(a)
    print(c)
    print(b)
elif (c>a) and (a>b):
    print(b)
    print(a)
    print(c)
elif (a>c) and (c>b):
    print(b)
    print(c)
    print(a)
elif (c>b) and (b>a):
    print(a)
    print(b)
    print(c)
elif (b>a) and (a>c):
    print(c)
    print(a)
    print(b)