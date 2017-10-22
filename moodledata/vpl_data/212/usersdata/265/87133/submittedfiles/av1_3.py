# -*- coding: utf-8 -*-
import math
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))
i=2
j=2
k=2
while i<=a:
    if a%i==0:
        da=i
    i=i+1
    break
print(da)
for i in range(2,a+1,1):
    if a%i==0:
        divisor_a=i
    break
