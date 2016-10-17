# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))

cont=0
while a%b>=0:
    cont=cont+1
    b=a%b
    a=b
    if b==0:
        break

print(a)
print(cont)
        