# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de c: '))

for i in range (1,c+1,1):
    if c%a==0:
        g=(c//a)
    elif c%b==0:
        h=c//b
    else:
        x=c//a
        y=(c%a)/b
    print(g)
    print(h)
    print(x)
    print(y)
    
