# -*- coding: utf-8 -*-
#ENTRADA
a = float(input('digite a: '))
b = float(input('digite b: '))
c = float(input('digite c: '))
#PROCESSAMENTO
if (a>b) and (b>c) and (c>a):
    print(c)
    print(b)
    print(a)
if (a>c) and (c<b) and (b>a):
    print(b)
    print(c)
    print(a)
if (b>c) and (c>a) and (a>b):
    print(a)
    print(c)
    print(b)
if (b>a) and (a>c) and (c>b):
    print(c)
    print(a)
    print(b)
if (c>b) and (b>a) and (a>c):
    print(a)
    print(b)
    print(c)
if (c>a) and (a>b) and (b>c):
    print(b)
    print(a)
    print(c)
