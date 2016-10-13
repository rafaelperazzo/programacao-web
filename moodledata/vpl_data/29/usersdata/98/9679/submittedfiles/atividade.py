# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n: '))

contador=0

while True:
    valor=n/10
    contador=contador+1
    n=n//10
    if n==0:
        break
print(contador)