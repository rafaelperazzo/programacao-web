# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('digite a:'))
b = int(input('digite a:'))

if a>=b:
    menor=b
elif a<=b:
    menor=a
i=menor
cont=0
while True:
    if a%i==0 and b%i==0:
        print(i)
        cont=cont+1
        break
    i=menor-1
print(cont)