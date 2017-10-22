# -*- coding: utf-8 -*-
import math
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))
i=2
j=2
k=2
p=0
while i<=a:
    if a%1==0:
        p=p+i
    i=i+1
print(p)
for i in range(2,a+1,1):
    if a%i==0:
        divisor_a=i
    break
