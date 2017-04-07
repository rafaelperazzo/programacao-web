# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if a>=b and b>=c and a>=d:
    print(a)
elif b>=a and b>=c and b>=d:
    print(b)
elif c>=a and c>=b and c>=d:
    print(c)
else:
    print(d)
if a<=b and a<=c and a<=d:
    print(a)
elif b<=a and b<=c and c<=d:
    print(b)
elif c<=a and c<=b and c<=d:
    print(c)
else:
    print(d)

