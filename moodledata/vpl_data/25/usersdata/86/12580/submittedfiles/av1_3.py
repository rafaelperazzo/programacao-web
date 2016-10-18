# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('digite a:'))
b = int(input('digite b:'))

if a>=b:
    menor=b
elif a<=b:
    menor=a
i=menor
cont=1
while True:
    if a%i==0 and b%i>=0:
        if a/i>0 and b/i>0:
            cont=cont+1
    i=i-1

print(i)
print(cont)