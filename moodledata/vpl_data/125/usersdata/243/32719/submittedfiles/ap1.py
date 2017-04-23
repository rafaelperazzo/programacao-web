# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))

if a<b and b<c:
    print(a)
    print(b)
    print(c)
    
elif a<c and c<b: 
    print(a)
    print(c)
    print(b)
elif b<c and c<a:
    print(c)
    print(a)
    print(b)
elif b<a and a<c:
    print(b)
    print(a)
    print(c)
else:
    print(c)
    print(a)
    pritn(b)