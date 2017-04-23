# -*- coding: utf-8 -*-
a=float(input('Digite um número:'))
b=float(input('Digite um número:'))
c=float(input('Digite um número:'))

if a<b and b<c:
    print (a)
    print (b)
    print (c)
elif a<c and c<b:
    print (a)
    print (c)
    print (b)
elif b<a and b<c:
    print (b)
    print (a)
    print (c)
elif b<c and c<a:
    print (b)
    print (c)
    print (a)
elif c<b and b<a:
    print (c)
    print (b)
    print (a)
else:
    print (c)
    print (a)
    print (b)
    