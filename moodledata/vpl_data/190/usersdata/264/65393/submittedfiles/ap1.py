# -*- coding: utf-8 -*-
#Entrada:
a= float(input('Digite o valor de a:'))
b= float(input('Digite o valor de b:'))
c= float(input('Digite o valor de c:'))
#Processamento:
if (a>b) and (b>c):
    print(c)
    print(b)
    print(a)
if (c>b) and (b>a):
    print(a)
    print(b)
    print(c)
if (a>c) and (c>b):
    print(b)
    print(c)
    print(a)
if (b>a) and (a>c):
    print(c)
    print(a)
    print(b)
if (b>c) and (c>a):
    print(a)
    print(c)
    print(b)
if (c>a) and (a>b):
    print(b)
    print(a)
    print(c)