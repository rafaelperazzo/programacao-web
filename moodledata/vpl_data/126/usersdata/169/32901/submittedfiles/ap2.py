# -*- coding: utf-8 -*-
a=int(input('Digite N1:'))
b=int(input('Digite N2:'))
c=int(input('Digite N3:'))
d=int(input('Digite N4:'))
if a>b and a>c and a>d:
    print(a)
elif b>a and b>c and b>d:
    print(b)
elif c>a and c>b and c>d:
    print(c)
else: 
    print(d)
if a<b and a<c and a<d:
    print(a)
elif b<a and b<c and b<d:
    print(b)
elif c<a and c<b and c<d:
    print(c)
else: 
    print(d)