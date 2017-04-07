# -*- coding: utf-8 -*-
a=float(input('digite um valor para a:'))
b=float(input('digite um valor para b:'))
c=float(input('digite um valor para c:'))
if a>b:
    print(a)
    if b>c:
        print(b)
    if c>b:
        print(c)
elif b>a:
    print(b)
    if a>c:
        print(a)
    if c>a:
        print(c)
else c>a:
    print c
    if a>b:
        print(a)
    if b>a:
        print(b)
        
        
        