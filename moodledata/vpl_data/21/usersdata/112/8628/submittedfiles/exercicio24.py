# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('Digite o valor de n:'))
m = int(input('Digite o valor de m:'))
minimo=1
divisor=2 
while divisor <= n:
    if n % divisor == 0 and m % divisor == 0:
        minimo = divisor
    divisor += 1 

print(minimo)