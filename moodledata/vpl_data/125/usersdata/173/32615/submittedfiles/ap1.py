# -*- coding: utf-8 -*-
a=float(input('Digite um número: '))
b=float(input('Digite um número: '))
c=float(input('Digite um número: '))
if(a<b<c):
    print(a)
    print(b)
    print(c)
elif(a<c<b):
    print(a)
    print(c)
    print(b)
elif(b<a<c):
    print(b)
    print(a)
    print(c)
elif(b<c<a):
    print(b)
    print(c)
    print(a)
elif(c<a<b):
    print(c)
    print(a)
    print(b)
else:
    print(c)
    print(b)
    print(a)