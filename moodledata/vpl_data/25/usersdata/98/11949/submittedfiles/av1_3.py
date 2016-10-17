# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
i=1
cont=0

while a%b>0:
    c=a/b
    a=c
    b=a%b
    cont+1
print(b)
print(cont)
        