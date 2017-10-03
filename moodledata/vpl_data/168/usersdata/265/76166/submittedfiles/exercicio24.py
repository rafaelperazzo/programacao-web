# -*- coding: utf-8 -*-
import math
a = int(input('digite o valro de a: '))
b = int(input('digite o valor de b: '))
i=1
while (i<=a):
    if (a%i==0) and (b%i==0):
        MDC=i
    i=i+1
print(MDC)
    