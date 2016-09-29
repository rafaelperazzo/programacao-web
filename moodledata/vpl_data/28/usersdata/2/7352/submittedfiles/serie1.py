# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Digite o valor de n:')

soma = 0
for i in range (1,n+1,1):
    soma = soma + i/(i**2)

print ("%.5f" % soma)
