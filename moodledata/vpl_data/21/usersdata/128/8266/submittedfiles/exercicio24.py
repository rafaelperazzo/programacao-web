# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))

if a>b:
    i=a
else:
    i=b

while True:
    if a%i==0 and b%i==0:
        print (i)
        break
        i=i+1
