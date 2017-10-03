# -*- coding: utf-8 -*-
import math
a = int(input('digite o valro de a: '))
b = int(input('digite o valor de b: '))
i=1
while (i<=a) and (i<=b):
    if (a%i==0):
        print(i)
        i=i+1
    if (b%i==0):
        i=i+1
        print(i)
        