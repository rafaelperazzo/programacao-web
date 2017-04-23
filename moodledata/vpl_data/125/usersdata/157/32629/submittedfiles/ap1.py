# -*- coding: utf-8 -*-
a=float(input("Digite o numero A: "))
b=float(input("Digite o numero B: "))
c=float(input("Digite o numero C: "))
if  (a<b<c):
    print (a)
    print (b)
    print (c)
elif (a<c<b):
    print (a)
    print (c)
    print (b)
elif (b<a<c):
    print (b)
    print (a)
    print (c)
elif (b<c<a):
    print (b)
    print (c)
    print (a)
elif (c<a<b):
    print (c)
    print (a)
    print (b)
else:
    print (c)
    print (b)
    print (a)