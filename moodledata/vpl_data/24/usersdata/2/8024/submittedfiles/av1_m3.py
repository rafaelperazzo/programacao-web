# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite m: ')

soma = 3
j = 2
for i in range(1,m+1,1):
    if i%2==1:
        soma = soma + 4/(j*(j+1)*(j+2))
    else:
        soma = soma - 4/(j*(j+1)*(j+2))
    j = j + 2
    print (4/(j*(j+1)*(j+2)))
print ("%.6f" % soma)
