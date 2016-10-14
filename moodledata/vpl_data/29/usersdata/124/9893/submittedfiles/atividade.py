# -*- coding: utf-8 -*-
from __future__ import division
import math

i = 0
n = int(input('Digite o valor de n: '))
while n > 0:
    n = n//10
    i = i+1
print(i)