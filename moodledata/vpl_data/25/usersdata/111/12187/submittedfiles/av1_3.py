# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite a: ')
b=input('Digite b: ')
if b>a:
    c=b
    d=a
else:
    c=a
    d=b
i=1
while True:
    c=(c%d)
    i=i+1
    d=(d%c)
    if d==0:
        print c
        break
    i=i+1
print i

