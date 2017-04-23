# -*- coding: utf-8 -*-
a = float(input('Digite a:'))
b = float(input('Digite b:'))
c = float(input('Digite c:'))
if a>b and a>c:
    print (a)
    elif b>a and b>c:
        print (b)
        else:
            print (c)
if a>b and a<c or a>c and a<b:
    print (a)
    elif b>a and b<c or b>c and b<a:
        print(b)
        else:
            print(c)
if a<b and a<c:
    print(a)
    elif b<a and b<c:
        print(b)
        else:
            print(c)