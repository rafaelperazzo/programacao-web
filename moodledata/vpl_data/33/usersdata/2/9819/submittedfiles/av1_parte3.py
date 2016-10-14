# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE AQUI ABAIXO
n = input('Digite o valor de n:')
pi = 0
for i in range(0,n+1,1):
    pi = pi + (-3**(-i))/(2*i+1)

pi = pi*math.sqrt(12)

print pi
