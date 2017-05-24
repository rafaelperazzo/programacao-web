# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if a>=b and a>=c and b>=c:
    print(a)
    print(b)
    print(c)
elif b>=a and b>=c and a>=c:
    print(b)
    print(a)
    print(c)
else:
    if c>=a and c>=b and a>=b:
        print(c)
        print(a)
        print(b)
    elif a>=b and a>=c and c>=b:
        print(a)
        print(c)
        print(b)
    else:
        if b>=a and b>=c and c>=a:
            print(b)
            print(c)
            print(a)
        elif c>=a and c>=b and b>=a:
            print(c)
            print(b)
            print(a)


