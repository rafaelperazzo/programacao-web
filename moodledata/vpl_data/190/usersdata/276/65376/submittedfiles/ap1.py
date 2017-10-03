# -*- coding: utf-8 -*-
a = float (input('Digite o valor de a: '))
b = float (input('Digite o valor de b: '))
c = float (input('Digite o valor de c: '))
if (a>b) and (b>c):
    print (c)
    print (b)
    print (a)
elif (a>c) and (c>b):
    print (b)
    print (c)
    print (a)
elif (b>a) and (a>c):
    print (c)
    print (a)
    print (b)
elif (b>c) and (c>a):
    print (a)
    print (c)
    print (b)
elif (c>a) and (a>b):
    print (b)
    print (a)
    print (c)
else (c>b) and (b>a):
    print (a)
    print (b)
    print (c)

