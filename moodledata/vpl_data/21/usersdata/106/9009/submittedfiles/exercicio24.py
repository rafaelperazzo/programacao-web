# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int (input('Digite o valor de a:'))
b = int (input('Digite o valor de b:'))
if a<=b:
    d = b
else:
    d = a
while True:
    if a%d == 0 and b%d == 0:
        print (d)
        break
    elif a%d!=0 or b%d!=0:
        d=d-1
    if d==1:
        print (d)
        break
            