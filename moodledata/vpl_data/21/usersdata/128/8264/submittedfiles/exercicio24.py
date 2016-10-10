# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))

i=1

while True:
    if a%i==0 and b%i==0:
        print (i)
        break
        i=i+1
