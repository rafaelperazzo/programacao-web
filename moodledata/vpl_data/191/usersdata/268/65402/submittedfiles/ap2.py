# -*- coding: utf-8 -*-
a=float(input('Digite o valor de a:'))
b=float(input('Digite o valor de b:'))
c=float(input('Digite o valor de c:'))
d=float(input('Digite o valor de d:'))

if (a>b) and (a>c) and (a>d):
    print(a)
elif (b>a) and (b>c) and (b>d):
    print(b)
elif (c>a) and (c>a) and (c>d):
     print(c)
elif (d>a) and (d>c) and (d>b):
     print(d)
elif (a<b) and (a<c) and (a<d):
    print(a)
elif (b<a) and (b<c) and (b<d):
    print(b)
elif (c<b) and (c<a) and (c<d):
    print(c)
elif (d<b) and (d<a) and (d<c):
    print(d)