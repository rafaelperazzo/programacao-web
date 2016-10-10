# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('digite o numero de termos: '))

soma = 0
i = 1
j = 1
while i<=n:
    if i%2 == 0:
        soma = soma - j/(j**2)
    else: 
        soma = soma + j/(j**2)
    print soma
j = j+1
i = i+1