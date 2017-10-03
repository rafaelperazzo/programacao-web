# -*- coding: utf-8 -*-
#ENTRADA
a = float(input('digite a: '))
b = float(input('digite b: '))
c = float(input('digite c: '))
#PROCESSAMENTO
if (a<b) and (b<c):
    print(a)
    print(b)
    print(c)
if (a<c) and (c<b):
    print(b)
    print(c)
    print(a)
if (b<c) and (c<a):
    print(b)
    print(c)
    print(a)
if (b<a) and (a<c):
    print(b)
    print(a)
    print(c)
if (c<b) and (b<a):
    print(c)
    print(b)
    print(a)
if (c<a) and (a<b):
    print(c)
    print(a)
    print(b)