# -*- coding: utf-8 -*-
import math

a= int(input('digite o valor de a:'))
b= int(input('digite o valor de b:'))
if a<b:
    menor= a
else:
    menor= b
for i in range(1, menor+ 1,1):
    if a% i ==0 and b% i==0:
        mdc= i
print(mdc)