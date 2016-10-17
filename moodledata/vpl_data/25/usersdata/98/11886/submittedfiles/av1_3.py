# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
i=1
cont=0
c=0
while True:
    if a%i==0 and b%i==0:
        cont=cont+1
        c=i
    i=i+1
    if i==a or i==b:
        break
print(c)
print(cont)