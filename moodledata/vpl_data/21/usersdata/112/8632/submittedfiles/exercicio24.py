# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
minimo=1
divisor=2 
while divisor <= a:
    if a % divisor == 0 and b % divisor == 0:
        minimo = divisor
    divisor = 1 

print(minimo)