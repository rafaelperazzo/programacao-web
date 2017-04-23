# -*- coding: utf-8 -*-
a=float(input('digite uma valor:'))
b=float(input('digite uma valor:'))
c=float(input('digite uma valor:'))
d=float(input('digite uma valor:'))

if (a>b) and (a>c) and (a>d):
    print(a)
elif(b>a) and (b>c) and (b>d):
    print(b)
elif (c>b) and (c>a) and (c>d):
    print(c)
else:
    print(d)
if (a<b) and (a<c) and (a<d):
    print(a)
elif(b<a) and (b<c) and (b<d):
    print(b)
elif (c<b) and (c<a) and (c<d):
    print(c)
else:
    print(d)

