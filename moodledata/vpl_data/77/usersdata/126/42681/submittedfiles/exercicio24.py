# -*- coding: utf-8 -*-
import math

a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))

i=1

for i in range(1,a+1,1):
    if i%a==0 and i%b==0:
        mdc=i
print(mdc)
