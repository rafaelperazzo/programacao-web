# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if  a<=b and a<=c:
    print(a)
    if b<=c:
    print (b)
    print (c)
    else:
    print(c)
    print(b)
elif b<=a and b<=c:
     if a<=c:
     print(a)
     print(c)
     else:
     print(c)
     print(a)
elif c<=a and c<=b:
     print(c)
     if a<=b:
     print(a)
     print(b)
     else:
     print(b)
     print(a)
