# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
i=1
cont=0

while True:

    c=a/b
    a=b
    b=a%b
    cont+1
    if a%b==0:
        break
print(b)
print(cont)
        