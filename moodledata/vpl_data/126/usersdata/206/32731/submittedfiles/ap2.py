# -*- coding: utf-8 -*-
a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
d=float(input('Digite d:'))

if(a>b) and (a>c) and (a>d):
    print(a)
elif(b>a) and (b>c) and (b>d):
    print(b)
elif(c>a) and (c>b) and (c>d):
    print(c)
else:
    print(d)
if(a<b) and (a<c) and (a<d):
    print(a)
elif(b<a) and (b<c) and (b<d):
    print(b)
elif(c<a) and (c<b) and (c<d):
    print(c)
else:
    print(d)
