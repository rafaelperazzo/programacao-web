# -*- coding: utf-8 -*-
import math

n = int(input('digite valor de n: '))
a = int(input('digite valor de n: '))
b = int(input('digite valor de n: '))

for i in range (2,(n+1),1):
    if a<b:
        print (a)
        print (b)
    else:
        print (b)
        print (a)
    a = a+a
    b = b+b
