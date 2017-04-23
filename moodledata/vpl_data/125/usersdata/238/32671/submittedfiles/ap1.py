# -*- coding: utf-8 -*-
a=float(input('digite o numero 1:'))
b=float(input('digite o numero 2:'))
c=float(input('digite o numero 3:'))
if (a<b) and (b>c):
    print(a)
    print(b)
    print(c)
elif(a<c) and (c>b):
    print(a)
    print(b)
    print(c)
elif(b<a) and (a>b):
    print(a)
    print(b)
    print(c)
  