# -*- coding: utf-8 -*-
a=float(input('digite um valor para a:'))
b=float(input('digite um valor para b:'))
c=float(input('digete um valor para c:'))
if a<=b and a<=c:
    print(a)
    if b<=c:
        print(b)
        print(c)
        else:
            print(c)
            print(b)
elif b<=a and b<=c:
    print(b)
    if a<=c:
        print(a)
        print(c)
        else:
            print(c)
            print(a)
else:
    print(c)
    if a<=b:
        print(a)
        print(b)
        else:
            print(b)
            print(a)
            
            