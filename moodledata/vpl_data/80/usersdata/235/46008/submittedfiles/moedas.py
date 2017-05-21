# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de A:'))
b=int(input('digite o valor de B:'))
c=int(input('digite o valor de C:'))
if a<0 or b<0 or c<0:
    print(N)
    if a>b:
        i=0
        while c>0:
            i=c//a
            i=i+1
            c=c//a
            print(i)
            if c<a:
                n=c//b
                n=n+1
                print(n)