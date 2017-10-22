# -*- coding: utf-8 -*-
import math
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))
j=2
k=2
for i in range (2,a+1,1):
    if a%i==0:
        divisora=i
        print(divisora)
    break

