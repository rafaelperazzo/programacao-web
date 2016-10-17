# -*- coding: utf-8 -*-
from __future__ import division
import math
dividendo=int(input('digite o valor de a='))
divisor=int(input('digite o valor de b='))
cont=1
resto=dividendo%divisor
while resto!=0:
    dividendo=divisor
    divisor=resto
    resto=divisor%resto
    cont=cont+1
print(resto)
print (cont)
