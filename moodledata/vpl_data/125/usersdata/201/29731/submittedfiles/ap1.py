# -*- coding: utf-8 -*-
a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
if a<=b and a<=c:
    print (a)
    if b<=c:
        print (b)
        print (c)
    else:
        print (c)
        print (b)
elif b<=a and b<=c:
    print (b)
    if a<=c:
        print (a)
        print (c)
    else:
        print (c)
        print (a)
else:
    print (c)
    if a<=b:
        print (a)
        print (b)