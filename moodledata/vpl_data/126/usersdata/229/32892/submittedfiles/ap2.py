# -*- coding: utf-8 -*-
a=(input('digite um valor a:'))
b=(input('digite um valor b:'))
c=(input('digite um valor c:'))
d=(input('digite um valor d:'))
if(a>b) and (a>c) and (a>d):
    print(a)
elif (b>a) and (b>c) and (b>d):
    print(b)
else:
    print(d)
if (a<b) and (a<c) and (a<d):
    print(a)
elif (b<a) and (b<c) and (b<d):
    print(b)
elif (c<a) and (c<b) and (c<d):
    print(d)