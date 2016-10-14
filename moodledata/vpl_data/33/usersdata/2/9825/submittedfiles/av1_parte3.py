# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE AQUI ABAIXO
n = input('Digite o valor de n:')
pi = 0
j = 1
for i in range(0,n+1,1):
    if i%2==0:
        pi = pi + 1/(j*(3**i))
    else:
        pi = pi - 1/(j*(3**i))
    j = j + 2

pi = pi*(12**0.5)

print ("%.6f" % pi)
