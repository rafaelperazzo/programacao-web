# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))

cont=0
while b!=0:
    if a%b>=0:
        cont=cont+1
        a=b
        b=a%b
print(a)
print(cont)
        