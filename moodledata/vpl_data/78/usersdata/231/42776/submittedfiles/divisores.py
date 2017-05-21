# -*- coding: utf-8 -*-
import math

a=int(input('digite valor de a :'))
b=int(input('digite valor de b :'))
n=int(input('digite valor de n :'))
for i in range(1,n+2,1):
    if i%a==0 and i%b==0:
        print(i)
    elif i%a==0:
        print(1)
    elif i%b==0:
        print(i)





