# -*- coding: utf-8 -*-
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
delta=(b**2)-(4*a*c)
if delta>0:
    x1=(-b+(delta)**(1/2))/(2*a)
    x2=(-b-(delta)**(1/2))/(2*a)
    print(x1)
    print(x2)
else:
    ('SSR')