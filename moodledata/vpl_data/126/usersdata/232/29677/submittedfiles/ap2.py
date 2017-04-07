# -*- coding: utf-8 -*-
a=int(input('Digite um valor para a: '))
b=int(input('Digite um valor para a: '))
c=int(input('Digite um valor para a: '))
d=int(input('Digite um valor para a: '))
if a<b<c<d:
    print(d)
    print(a)
if a<b<d<c:
    print(c)
    print(a)
if a<c<b<d:
    print(d)
    print(a)
if a<d<c<b:
    print(b)
    print(a)
if a<c<d<b:
    print(b)