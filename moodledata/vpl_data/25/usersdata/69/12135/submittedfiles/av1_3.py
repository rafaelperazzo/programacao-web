# -*- coding: utf-8 -*-
from __future__ import division
import math
dividendo=int(input('digite o valor de dividendo='))
divisor=int(input('digite o valor de divisor='))
cont=1
resto=dividendo%divisor
while resto!=0:
    dividendo=divisor
    divisor=resto
    resto=dividendo%divisor
    cont=cont+1
print(resto)
print (cont)
