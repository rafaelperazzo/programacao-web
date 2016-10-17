# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=0
cont=0
while a%b>=0:
    c=a%b
    cont=cont+1
    a=b
    b=c
    if b==0: 
        break
print(a)
print(cont)
        