# -*- coding: utf-8 -*-
a=float(input('digite o 1° número:'))
b=float(input('digite o 2° número:'))
c=float(input('digite o 3° número:'))
if  a<=b and a<=c:
    print(a)
    if  b<=c:
        print(b)
        print(c) 
    else    :
        print(c)
        print(b)
elif    b<=a and b<=c:
        print(b)
        if  a<=c:
            print(a)
            print(c)
        else    :
            print(c)
            print(a)

