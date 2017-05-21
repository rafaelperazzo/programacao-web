# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de c: '))

for i in range (1,c+1,1):
    if (c%a)==0:
        g=(c//a)
        print(g)
    elif (c%b)==0:
        h=(c//b)
        print(h)
    elif (c%a)!=0
        x=(c%a)
        y=(c%a)//b
        print(x)
        print(y)
    elif (c%b) !=0:
        x=(c%a)
        y=(c%a)//b
        print(x)
        print(y)
    else:
        print('N')
