# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite um valor n:'))
contador=0

while n>0:
    n=n//10
    contador=contador+1
print(contador)