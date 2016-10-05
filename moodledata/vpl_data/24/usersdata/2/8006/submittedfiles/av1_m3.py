# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite m: ')

soma = 3

for i in range(1,m+1,1):
    if i%2==1:
        soma = soma + 4/((i+1)*(i+2)*(i+3))
    else:
        soma = soma - 4/((i+1)*(i+2)*(i+3))

print ("%.6f" % soma)
