# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('Digite n:'))

soma = 0
for j in range(1, n +1,1):
    soma = soma + (j/n)
    n = n - 1
print(soma)