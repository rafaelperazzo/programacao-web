# -*- coding: utf-8 -*-
a=int(input("Digite um numero (a): "))
b=int(input("Digite um numero (b): "))
c=int(input("Digite um numero (c): "))
if a<b<c:
    print (a)
elif b<c<a:
    print (b)
elif c<a<b:
    print (c)
elif b<a<c:
    print (b)
elif a<c<b:
    print (a)
elif c<a<b:
    print (c)