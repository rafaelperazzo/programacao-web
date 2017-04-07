# -*- coding: utf-8 -*-
a= float(input('digite a:'))
b= float(input('digite b:'))
c= float(input('digite c:'))
if a>b and a>c and b>c:
    print(a,b,c)
if b>a and b>c and a>c:
    print(b,a,c)
if c>a and c>b and b>a:
    print(c,b,a)