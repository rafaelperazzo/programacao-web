# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if a>b and b>c and a>c:
    print(a)
    print(b)
    print(c)
if a>b and c>b and a>c:
    print(a)
    print(c)
    print(b)
if a>b and c>a and c>b:
    print(c)
    print(a)
    print(b)
if b>a and c>a and c>b:
    print(c)
    print(b)
    print(a)
if b>a and a>c and b>c:
    print(b)
    print(a)
    print(c)
if b>a and c>a and b>c:
    print(b)
    print(c)
    print(a)
if b=a or a=c or b=c:
    print('numeros iguais')
    
