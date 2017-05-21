# -*- coding: utf-8 -*-
import math
a=int(input('digite um valor:'))
b=int(input('digite um valor:'))
if a<b:
    for i in range(1,a+1,1):
        if a%i==0 and b%i==0:
            divisor=i
    print(divisor)
if a>b:
    for i in range(1,a+1,1):
        if a%i==0 and b%i==0:
            divisor=i
    print(divisor)    

