# -*- coding: utf-8 -*-
a=float(input('Digite o primeiro número:'))
b=float(input('Digite o segundo número:'))
c=float(input('Digite o terceiro número:'))

if a>b and b>c:
    print(c%b&a)
if b>a and a>c:
    print(c%a%b)
if c>b and b>a:
    print(a%b%c)
if c>a and a>c:
    print(b%a%c)
if b>c and c>a:
    print (a%c%b)
if a>c and c>b:
    print (b%c%a)