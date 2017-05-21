# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite moedas:'))
b=int(input('digite moedas:'))
c=int(input('cedulass:'))
a1=0
b1=0
while c>=0:
    if c>=a:
        x=c/a
        c=c-a
        a1=a1+1
    if c>=b:
        y=c/b
        c=c-b
        b1=b+1
print(x)
print(y)






