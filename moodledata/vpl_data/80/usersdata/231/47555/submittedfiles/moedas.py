# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite moedas:'))
b=int(input('digite moedas:'))
c=int(input('cedulass:'))
while c>=0:
    if c>=a:
        x=c/a
        c=c-a
    if c>=b:
        y=c/b
        c=c-b
print(x)
print(y)






