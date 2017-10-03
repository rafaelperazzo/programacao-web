# -*- coding: utf-8 -*-
a = int(input('Digite um número inteiro: '))
b = int(input('Digite um número inteiro: '))
c = int(input('Digite um número inteiro: '))

if (a==b) and (b==c):
    print(a)
if (a==b) and (b<c):
    print(a)
if (a==c) and (c<b):
    print(a)
if (a<b) and (b<c):
    print(a)
if (a<c) and (c<b):
    print(a)
if (b==c) and (c<a):
    print(b)
if (b<c) and (c<a):
    print(b)
if (b<a) and (a<c):
    print(b)
if (c<b) and (b<a):
    print(c)
if (c<a) and (a<b):
    print(c)