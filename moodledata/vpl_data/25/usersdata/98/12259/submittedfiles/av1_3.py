# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=0
cont=0
while c%b>=0:
        cont=cont+1
        c=b
        b=a%b
print(c)
print(cont)
        