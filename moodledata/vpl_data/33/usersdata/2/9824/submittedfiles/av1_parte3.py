# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE AQUI ABAIXO
n = input('Digite o valor de n:')
pi = 0
for i in range(0,n+1,1):
    pi = pi + ((-1/3)**i)/(2*i+1)

pi = pi*(12**0.5)

print ("%.6f" % pi)
