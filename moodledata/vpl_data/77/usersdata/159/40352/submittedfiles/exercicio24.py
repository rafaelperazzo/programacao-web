# -*- coding: utf-8 -*-
import math
a=int(input('Digite a:'))
b=int(input('Digite b:'))

if a<=b:
    x=a
else:
    x=b
i=1
while i<=x:
    if a%i==0 and b%i==0:
        divisor=i
    i=i+1
print(divisor)    