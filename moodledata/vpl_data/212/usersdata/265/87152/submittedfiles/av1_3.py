# -*- coding: utf-8 -*-
import math
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))
i=2
j=2
k=2
d=0
while i<=a:
    if a%i==0:
        d=d+i
    i=i+1
    print(d)
    break