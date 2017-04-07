# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if a<b and a<c:
    print(a)
elif b<c:
    print(b)
    print(c)
else:
    print(a)
    print(b)
    print(c)
elif c<b:
    print(c)
    print(b)
else:
    print(a)
    print(c)
    print(b)
if b<a and b<c:
    print(b)
elif a<c:
    print(a)
    print(c)
else:
    print(b)
    print(a)
    print(c)
elif c<a:
    print(a)
    print(c)
else:
    print(b)
    print(c)
    print(a)
if c<a and c<b:
    print(c)
elif a<b:
    print(a)
    print(b)
else:
    print(c)
    print(a)
    print(b)
elif b<a:
    print(b)
    print(a)
else:
    print(c)
    print(b)
    print(a)