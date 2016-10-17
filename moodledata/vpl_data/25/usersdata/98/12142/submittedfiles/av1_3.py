# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
i=1
cont=0
c=0
while True:
    if a%b>=0:
        cont=cont+1
        a=b
        b=a%b
    if b==0:
        break
print(a)
print(cont)
        