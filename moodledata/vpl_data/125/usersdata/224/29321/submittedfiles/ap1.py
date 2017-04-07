# -*- coding: utf-8 -*-
a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
if a<=b and a<=c:
    print(a)
    if b<=c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif  b<=a and b<=c:
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
        