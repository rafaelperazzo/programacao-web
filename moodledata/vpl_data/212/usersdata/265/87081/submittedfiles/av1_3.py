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
        divisor_a=i
    i=1+i
print(i)
while j<=b:
    if b%j==0:
        divisor_b=j
    j=1+j
print(j)
while k<=c:
    if c%k==0:
        divisor_c=k
    k=1+k
print(k)