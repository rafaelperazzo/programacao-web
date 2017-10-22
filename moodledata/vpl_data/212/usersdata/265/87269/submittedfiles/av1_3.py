# -*- coding: utf-8 -*-
import math
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))
i=2
j=2
k=2
while i<=a and j<=b and k<=c:
    if a%i==0:
        divisor_a=i
        break
    i=i+1
    print(divisor_a)