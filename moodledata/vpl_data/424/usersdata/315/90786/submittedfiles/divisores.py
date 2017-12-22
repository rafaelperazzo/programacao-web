# -*- coding: utf-8 -*-
import math

n = int(input('digite valor de n: '))
a = int(input('digite valor de n: '))
b = int(input('digite valor de n: '))
a1 = a
b1 = a

for i in range (0,3,1):
    if a<b:
        print (a1)
        print (b1)
    else:
        print (b1)
        print (a1)
    a1 = a+a
    b1 = b+b
